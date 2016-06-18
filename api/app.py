import re, csv, itertools

from flask import Flask, jsonify
from flask_cors import CORS
from pprint import pprint as pp
app = Flask(__name__)
CORS(app)

from data import REVERSED_GENDER, REVERSED_DISCIPLINES, DISCIPLINES

amount_metric_regex = re.compile(r"(?P<amount>\d+)(?:\s)?(?P<metric>meter|m|kilogram|kg)")

# with open("olympic_events_2012.csv") as f:
#     reader = csv.DictReader(f)
#     events = [row for row in reader]

# discipline_names = set([event['discipline_name'].lower() for event in events])

@app.route("/")
def root():
    return "root"

@app.route("/<query>")
def query(query):
    query = query.lower()
    status = {}

    posessive_gender = [x + "'s" for x in REVERSED_GENDER.keys()]
    plain_gender = REVERSED_GENDER.keys()
    gender_candidates = itertools.chain(posessive_gender, plain_gender)

    for gender in gender_candidates:
        if gender in query:
            query = re.sub(r"\s\s+", " ", query.replace(gender, "").strip())
            status['gender'] = REVERSED_GENDER[gender.replace("'s", "")]
            status['rest'] = query

    posessive_discipline = [x + "'s" for x in REVERSED_DISCIPLINES.keys()]
    plain_discipline = REVERSED_DISCIPLINES.keys()
    discipline_candidates = itertools.chain(posessive_discipline, plain_discipline)

    for discipline_name in discipline_candidates:
        if discipline_name in query:
            query = re.sub(r"\s\s+", " ", query.replace(discipline_name, "").strip())
            status['discipline_code'] = REVERSED_DISCIPLINES[discipline_name.replace("'s", "")]
            status['discipline_name'] = DISCIPLINES[status['discipline_code']][0]
            status['rest'] = query

    m = amount_metric_regex.match(query)
    if m:
        amount_metric_dict = m.groupdict()
        status.update(amount_metric_dict)
        query = re.sub(r"\s\s+", r"\s", query.replace(m.group(), "").strip())
        status['rest'] = query

    return jsonify(status)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
