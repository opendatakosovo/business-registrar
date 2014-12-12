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
        business_registrar = {}
        business_registrar = business_form.data

        json_obj = {}
        json_obj = {
            'picture': business_registrar['picture'],
            'company_name': business_registrar['company_name'],
            'owner': business_registrar['owner'],
            'business_nr': business_registrar['business_nr'],
            'fiscal_nr': business_registrar['fiscal_nr'],
            'activity': business_registrar['activity'],
            'sector': business_registrar['sector'],
            'sector_c': business_registrar['sector_c'],
            'statuti_bisnesit': business_registrar['statuti_bisnesit'],
            'registration_date': business_registrar['registration_date'],
            'kontaktet': {
                'phone_nr': business_registrar['phone_nr'],
                'email': business_registrar['email'],
                'website': business_registrar['website'],
                'facebook': business_registrar['facebook'],
                'twitter': business_registrar['twitter'],
            },
            'lokacioni': {
                'address': business_registrar['address'],
                'city': business_registrar['city'],
                'kordinatat': {
                    'longitude': business_registrar['longitude'],
                    'latitude': business_registrar['latitude'],
                }
            },
            'specialiteti': business_registrar['specialiteti'],
            'other_information': business_registrar['other_information'],
        }

        mongo.db.business.update(
            {'_id': doc_id},
            {'$set': json_obj},
            True
        )
