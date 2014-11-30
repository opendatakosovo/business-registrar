from flask import render_template
from br.views.forms.indexform import IndexForm
from flask.views import MethodView


class Index(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        ''' Dispatch request
        '''
        form = IndexForm()
        return render_template('index.html', form=form)

    def post(self):
        '''process data and save them in database
        '''
        form = IndexForm()
        return render_template('index.html', form=form)
