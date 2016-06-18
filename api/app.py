import re, csv, itertools

from flask import Flask, jsonify
from flask_cors import CORS
from pprint import pprint as pp
app = Flask(__name__)
CORS(app)

from data import reverse_dict
from data import GENDER, DISCIPLINES, DOUBLES_VS_SINGLES, INDIVIDUAL_VS_TEAM
from data import SWIM_EVENTS, EQUESTRIAN_EVENTS, TRACK_EVENTS

amount_metric_regex = re.compile(r"(?P<amount>\d+)(?:\s)?(?P<metric>meter|m|kilogram|kg)")

with open("../olympic_events_2012.csv") as f:
    reader = csv.DictReader(f)
    events = [row for row in reader]

def string_found(string1, string2):
   if re.search(r"\b" + re.escape(string1) + r"\b", string2):
      return True
   return False

def search(status):
    filtered_events = events
    if status.get('discipline_name'):
        filtered_events = [event for event in filtered_events
            if event['discipline_name'].lower() == status['discipline_name']]
    if status.get('gender'):
        filtered_events = [event for event in filtered_events
            if string_found(status['gender'], event['olympic_event_name'].lower()) or
               string_found(status['gender'] + "'s", event['olympic_event_name'].lower())]
    if status.get('individual_team_type'):
        filtered_events = [event for event in filtered_events
            if status['individual_team_type'] in event['olympic_event_name'].lower()]
    return filtered_events

def parse(query):
    query = query.lower()
    status = {}

    print("searching for gender...")
    for gender in GENDER['women'] + GENDER['men'] + GENDER['mixed']:
        if gender in query:
            print("found gender %s" % gender)
            query = re.sub(r"\s\s+", " ", query.replace(gender, "").strip())
            status['gender'] = reverse_dict(GENDER)[gender]
            status['rest'] = query

    print("searching for discipline_name...")
    for discipline_name in reverse_dict(DISCIPLINES).keys():
        if discipline_name in query:
            print("found discipline_name %s" % discipline_name)
            query = re.sub(r"\s\s+", " ", query.replace(discipline_name, "").strip())
            status['discipline_code'] = reverse_dict(DISCIPLINES)[discipline_name.replace("'s", "")]
            status['discipline_name'] = DISCIPLINES[status['discipline_code']][0]
            status['rest'] = query

    print("searching for swim event...")
    for swim_event in reverse_dict(SWIM_EVENTS).keys():
        if swim_event in query:
            query = re.sub(r"\s\s+", " ", query.replace(swim_event, "").strip())
            status['swim_event'] = swim_event
            status['rest'] = query

    print("searching for equestrian event...")
    for equestrian_event in reverse_dict(EQUESTRIAN_EVENTS).keys():
        if equestrian_event in query:
            query = re.sub(r"\s\s+", " ", query.replace(equestrian_event, "").strip())
            status['equestrian_event'] = equestrian_event
            status['rest'] = query

    print("searching for track event...")
    for track_event in reverse_dict(TRACK_EVENTS).keys():
        if track_event in query:
            query = re.sub(r"\s\s+", " ", query.replace(track_event, "").strip())
            status['track_event'] = track_event
            status['rest'] = query

    print("searching for doubles vs singles...")
    for double_single_type in reverse_dict(DOUBLES_VS_SINGLES).keys():
        if double_single_type in query:
            query = re.sub(r"\s\s+", " ", query.replace(double_single_type, "").strip())
            status['double_single_type'] = double_single_type
            status['rest'] = query

    print("searching for individual vs team...")
    for individual_team_type in reverse_dict(INDIVIDUAL_VS_TEAM).keys():
        if individual_team_type in query:
            query = re.sub(r"\s\s+", " ", query.replace(individual_team_type, "").strip())
            status['individual_team_type'] = individual_team_type
            status['rest'] = query

    print("searching for amount and unit...")
    m2 = amount_metric_regex.search(query)
    if m2:
        amount_metric_dict = m2.groupdict()
        print("found amount metrix %s" % str(amount_metric_dict))
        print(amount_metric_dict)
        status.update(amount_metric_dict)
        query = re.sub(r"\s\s+", r"\s", query.replace(m2.group(), "").strip())
        status['rest'] = query

    return status

# with open("olympic_events_2012.csv") as f:
#     reader = csv.DictReader(f)
#     events = [row for row in reader]

# discipline_names = set([event['discipline_name'].lower() for event in events])

@app.route("/")
def root():
    return jsonify({})

@app.route("/<q>")
def foo(q):
    try:
        status = parse(q)
    except Exception as e:
        return jsonify({"error": str(e)})

    try:
        filtered_events = search(status)
    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({
        "meta": {"num": len(filtered_events)},
        "status": status,
        "events": filtered_events
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
