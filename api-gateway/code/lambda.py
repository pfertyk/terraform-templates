import os

import requests


def main(event, context):
    print(os.environ.get("MESSAGE", "No message found in env vars!"))
    response_json = requests.get("https://catfact.ninja/fact").json()
    if "body" in event:
        response_json["body"] = event["body"]
    return response_json
