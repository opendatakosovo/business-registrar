from flask import render_template
from flask.views import MethodView
from br import mongo



class List(MethodView):
    methods = ['GET']

    def get(self):
        ''' Dispatch request
        '''
        places = mongo.db.business.find();
        return render_template('list.html', places=places)