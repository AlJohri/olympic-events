import re, csv, itertools, logging
from collections import OrderedDict

from flask import Flask, jsonify

from flask_cors import CORS
from pprint import pprint as pp
app = Flask(__name__)
CORS(app)

app.config["JSON_SORT_KEYS"] = False

from data import reverse_dict
from data import GENDERS, DISCIPLINES, DOUBLES_VS_SINGLES, INDIVIDUAL_VS_TEAM
from data import SWIM_EVENTS, EQUESTRIAN_EVENTS, TRACK_EVENTS

amount_metric_regex = re.compile(r"(?P<amount>[\d,]+)(?:\s)?(?P<metric>meter|m|kilogram|kg)")

def string_found(string1, string2):
    # custom word boundary, r"\b" doesn't handle contractions properly
    if re.search(r"(?:^|\s|\n)(%s)(?:$|\s)" % re.escape(string1), string2):
        return True
    return False

def search(status):
    rest = status.pop('rest') if status.get('rest') != None else ""
    filtered_events = []
    for event, tagged_event in tagged_events:
        if all(tagged_event.get(k) == v for k,v in status.items()):
            filtered_events.append(event)
    return filtered_events

    # if status.get('discipline'):
    #     filtered_events = [event for event in filtered_events
    #         if event['discipline_name'].lower() == status['discipline_name']]
    # if status.get('gender'):
    #     filtered_events = [event for event in filtered_events
    #         if string_found(status['gender'], event['olympic_event_name'].lower()) or
    #            string_found(status['gender'] + "'s", event['olympic_event_name'].lower())]
    # if status.get('individual_team_type'):
    #     filtered_events = [event for event in filtered_events
    #         if status['individual_team_type'] in event['olympic_event_name'].lower()]
    

def search_for_dict_in_query(d, query, key, status):
    """
    search among a variety of different ways to say a particular entity
    starting from the longest variation and stopping after the first
    variation is found
    """
    logging.debug("searching for %s..." % key)
    revsersed_d = reverse_dict(d)
    for phrase in sorted(revsersed_d.keys(), key=len, reverse=True):
        if string_found(phrase, query):
            # print("found %s %s" % (key, phrase))
            query = re.sub(r"\b%s\b" % phrase, "", query).strip()
            query = re.sub(r"\s\s+", " ", query)
            status[key] = revsersed_d[phrase]
            status['rest'] = query
            break
    return query

def parse(query):
    query = query.lower()
    status = {}

    query = search_for_dict_in_query(GENDERS, query, "gender", status)
    query = search_for_dict_in_query(DISCIPLINES, query, "discipline", status)

    logging.debug("searching for amount and unit...")
    m2 = amount_metric_regex.search(query)
    if m2:
        amount_metric_dict = m2.groupdict()
        # print("found amount metrix %s" % str(amount_metric_dict))
        # print(amount_metric_dict)
        status.update(amount_metric_dict)
        query = re.sub(r"\s\s+", r"\s", query.replace(m2.group(), "").strip())
        status['rest'] = query

    query = search_for_dict_in_query(SWIM_EVENTS, query, "swim_event", status)
    # if status.get('swim_event'):
    #     if status.get('discipline') in ["SWIMMING", None]:
    #         status['discipline'] = "SWIWMMING"
    #     else:
    #         raise Exception("conflicting disciplines")

    query = search_for_dict_in_query(EQUESTRIAN_EVENTS, query, "equestrian_event", status)
    # if status.get('equestrian_event'): status['discipline'] = "EQUESTRIAN"

    query = search_for_dict_in_query(TRACK_EVENTS, query, "track_event", status)
    # if status.get('track_event'): status['discipline'] = "TRACK_AND_FIELD"

    query = search_for_dict_in_query(DOUBLES_VS_SINGLES, query, "doubles_singles", status)
    query = search_for_dict_in_query(INDIVIDUAL_VS_TEAM, query, "individuals_team", status)

    return status

# with open("olympic_events_2012.csv") as f:
#     reader = csv.DictReader(f)
#     events = [row for row in reader]

# discipline_names = set([event['discipline_name'].lower() for event in events])

@app.route("/")
def root():
    return "ok"

@app.route("/api/v1/query/", defaults={'q': ""})
@app.route("/api/v1/query/<q>")
def foo(q):
    try:
        status = parse(q)
    except Exception as e:
        return jsonify({"error": str(e)})

    try:
        filtered_events = search(status)
    except Exception as e:
        return jsonify({"error": str(e)})

    ret = OrderedDict((
            ("meta", {"num": len(filtered_events)}),
            ("status", status),
            ("events", filtered_events)))

    if len(filtered_events) > 40:
        del ret['events']
        ret['meta']['warning'] = "more than 40 events"

    return jsonify(ret)

if __name__ == "__main__":

    with open("../olympic_events_2012.csv") as f:
        reader = csv.DictReader(f)
        events = [row for row in reader]

    tagged_events = [(event, parse(event['discipline_name'] + " " + event['olympic_event_name'])) for event in events]
    # for event, tagged_event in tagged_events:
    #     print(event, tagged_event)

    app.run(host='0.0.0.0', debug=True)
