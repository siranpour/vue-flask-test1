#!/usr/bin/env python3

from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'

import sqlalchemy as db

from aq.core.extraction import DataArchive
from aq.core.retreival import ReQATools

# testing
host = "database-1.cluster-cae7cqi3hwtw.us-east-2.rds.amazonaws.com"
username = "postgresql"
password = "w210w210"
dbname = "test"
#db_engine = db.create_engine(f"postgresql+psycopg2://{host}:{username}@{password}")
#connection = db_engine.connect()
#
#

archive = DataArchive()
archive.load("./w207.zip.bz2")
reqa = ReQATools(archive)

@app.route("/dataentry", methods=["POST"])
def submitData():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()

        user_query = post_data.get('question')
        query = user_query if user_query.endswith('?') else user_query + '?'
        print(query)

        candidate_answers = reqa.do_reqa(query, 1)

        """
        TODO:
        - generate config object parameters for handler_store_op
        - invoke thread pool executor on handler_store_op
        - format handler_store_op response data as response_object to return to frontend
        """

        response_object = {
            "query": query,
            "response_candidates": []
        }
        for idx, candidate in enumerate(candidate_answers):
            hour = int(candidate['timestamp'] // 3600)
            min = int(candidate['timestamp'] // 60)
            sec = int(candidate['timestamp'] % 60)

            response_candidate = {}
            response_candidate['context'] = candidate['context']
            response_candidate['result'] = candidate["answer_pred"]
            response_candidate['timestamp_hms'] = f"{hour}:{min}:{sec}"
            response_candidate['timestamp'] = candidate["timestamp"]
            response_candidate['audio_title'] = candidate["source_id"]

            response_object["response_candidates"].append(response_candidate)

        print(response_object)
        return jsonify(response_object)


def handler_store_op(config):
    """
    TODO:
    1. convert parser cmd line arguments into config object
    2. find model code and invoke model on config object parameters
    3. define model output format/response
    """


if __name__ == '__main__':
    app.run(debug=True)