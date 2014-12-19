from flask import Response
from flask.views import View
from bson import json_util
from br import mongo

class Places(View):

    def dispatch_request(self, category=None):
    	methods = ['GET']

    	result = None

    	if category == None:
    		result = mongo.db.businesses.find()
    	else:
    		result = mongo.db.businesses.find({'activities': category})

        # Build response object.
        resp = Response(
            response=json_util.dumps(result),
            mimetype='application/json')

        # Return response.
        return resp