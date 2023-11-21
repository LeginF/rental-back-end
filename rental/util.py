import json
from decimal import Decimal

def buildResponse(statusCode, body=None):
    response = {
        'statusCode' : statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body, cls=CustomEncoder)
    return response

class CustomEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, Decimal):
            return float(obj)
        
        return json.J.default(self, obj)