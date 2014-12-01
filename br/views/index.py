from flask import render_template, request, redirect, url_for
from br.views.forms.indexform import IndexForm
from flask.views import MethodView
from br import mongo
from br.utils.utils import Utils

utils = Utils()


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

        #get the doc ID from utils
        doc_id = utils.get_doc_id()
        #save business form
        self.save_business_form(doc_id)

        return redirect(url_for('index'))

    def save_business_form(self, doc_id):

        # Update the patient doc with treatment.
        business_form = IndexForm(request.form)
        business_registrar = business_form.data

        mongo.db.business.update(
            {'_id': doc_id},
            {'$set': {'businessRegistration': business_registrar}},
            True
        )
