#!/usr/bin/env python3

from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/dataentry", methods=["POST"])
def submitData():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()

        user_query = post_data.get('question')
        print(user_query)

        """
        TODO:
        - generate config object parameters for handler_store_op
        - invoke thread pool executor on handler_store_op
        - format handler_store_op response data as response_object to return to frontend
        """

        response_object['result'] = 'yyyeeeaahhh!'
        response_object['timestamp'] = 'timestampvargoeshere'
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