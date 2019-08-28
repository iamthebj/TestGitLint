import json

from flask import Flask, request, json
import requests

app = Flask(__name__)
apiurl = " "

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/lint/", methods=['GET', 'POST', 'HEAD'])
def checker():
    if request.headers['Content-Type'] == 'application/json':
        pull = json.dumps(request.json)
        payload = json.loads(pull)
        if not payload['action'] == 'closed':
            pull_number = payload['number']
            apiurl = payload['pull_request']['url']
            return apiurl
