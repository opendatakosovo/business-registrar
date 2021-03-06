from flask import render_template, request, redirect, url_for
from br.views.forms.businessregistrationform import BusinessRegistrationForm
from flask.views import MethodView
from br import mongo
from br.utils.utils import Utils
from datetime import datetime

utils = Utils()

class BusinessRegistration(MethodView):
    methods = ['GET', 'POST']

    def get(self, doc_id=None):
        ''' Dispatch request
        '''
        form = BusinessRegistrationForm()

        # Populate form if we are retrieve it to edit a business
        if doc_id != None:
            doc = mongo.db.businesses.find_one({'_id': doc_id})

            form.doc_id.data = doc_id
            form.picture_outside.data = doc['picture']['outside']
            form.picture_inside.data = doc['picture']['inside']
            form.picture_panorama.data = doc['picture']['panorama']
            form.business_type.data = doc['business_type']
            form.business_name.data = doc['business_name']
            form.owner.data = doc['owner']
            form.business_nr.data = doc['business_nr']
            form.fiscal_nr.data = doc['fiscal_nr']
            form.activities.data = doc['activities']

            form.sector.data = doc['sector']['primary']
            if 'secondary' in doc['sector']:
                form.sector_c.data = doc['sector']['secondary']
            
            form.business_statute.data = doc['business_statute']
            
            date_iso = doc['registration_date']
            date_str = date_iso.strftime('%d/%m/%Y')
            form.registration_date.data = date_str

            form.phone_nr.data = doc['contacts']['phone_nr']
            form.email.data = doc['contacts']['email']
            form.website.data = doc['contacts']['website']
            form.facebook.data = doc['contacts']['facebook']
            form.twitter.data = doc['contacts']['twitter']
            form.address.data = doc['location']['address']
            form.city.data = doc['location']['city']
            form.latitude.data = doc['location']['coordinates']['latitude']
            form.longitude.data = doc['location']['coordinates']['longitude']
            form.speciality.data = doc['speciality']
            form.other_information.data = doc['other_information']

        return render_template('index.html', form=form)

    def post(self, doc_id=None):
        '''process data and save them in database
        '''
        #get the doc ID from utils
        if doc_id == None:
            doc_id = utils.get_doc_id()

        #save business form
        self.save_business_form(doc_id)

        return redirect(url_for('list'))

    def save_business_form(self, doc_id):
 
        # Update the patient doc with treatment.
        business_form = BusinessRegistrationForm(request.form)
        business_registrar = {}
        business_registrar = business_form.data

        if business_registrar['registration_date'] != "":
            date_string = business_registrar['registration_date']
            date = datetime.strptime(date_string, '%d/%m/%Y')

        print 'AAAA'
        print business_registrar['latitude']

        json_obj = {
            'picture':{
                'outside': business_registrar['picture_outside'],
                'inside': business_registrar['picture_inside'],
                'panorama': business_registrar['picture_panorama']
            },
            'business_type': business_registrar['business_type'],
            'business_name': business_registrar['business_name'],
            'owner': business_registrar['owner'],
            'business_nr': business_registrar['business_nr'],
            'fiscal_nr': business_registrar['fiscal_nr'],
            'activities': business_registrar['activities'],
            'business_statute': business_registrar['business_statute'],
            'registration_date': date,
            'contacts': {
                'phone_nr': business_registrar['phone_nr'],
                'email': business_registrar['email'],
                'website': business_registrar['website'],
                'facebook': business_registrar['facebook'],
                'twitter': business_registrar['twitter'],
            },
            'location': {
                'address': business_registrar['address'],
                'city': business_registrar['city'],
                'coordinates': {
                    'latitude': business_registrar['latitude'],
                    'longitude': business_registrar['longitude']
                }
            },
            'speciality': business_registrar['speciality'],
            'other_information': business_registrar['other_information'],
        }

        sector = business_registrar['sector']
        sector_c = business_registrar['sector_c']

        if sector == 'C. Processing Industry' and sector_c != "None":
            json_obj['sector'] = {
                'primary': sector,
                'secondary': sector_c,
            }
        else:
            json_obj['sector'] = {
                'primary':sector
            }

        mongo.db.businesses.update(
            {'_id': doc_id},
            {'$set': json_obj},
            True
        )
