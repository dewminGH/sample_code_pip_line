import json


def hello(event, context):
    body = {
        "message": "pip2XXX Go Serverless v4.0! Your function executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}
