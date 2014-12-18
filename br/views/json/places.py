from flask import Response
from flask.views import View
from bson import json_util
from br import mongo

class Places(View):

    def dispatch_request(self):
    	methods = ['GET']

    	result = mongo.db.businesses.find();

        # Build response object.
        resp = Response(
            response=json_util.dumps(result),
            mimetype='application/json')

        # Return response.
        return resp