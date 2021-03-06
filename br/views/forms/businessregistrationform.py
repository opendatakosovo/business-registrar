#-*- coding: utf-8 -*-
# import this module to recognize non-ASCII characters
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask_wtf import Form
from wtforms import FileField, TextField, TextAreaField, SelectField, IntegerField, SelectMultipleField, HiddenField, FloatField


class BusinessRegistrationForm(Form):

    doc_id = HiddenField()

    picture_outside = TextField('Fotoja e Jashtme e Kompanise')
    picture_inside = TextField('Fotoja e Mbrendshme e Kompanise')
    picture_panorama = TextField('Fotoja Panorame e Kompanise')

    business_type = SelectField(
        "Tipi Biznesit",
        choices=[
            ('Other', 'Other'),
            ('D.P.H.', 'D.P.H.'),
            ('D.P.T.', 'D.P.T.'),
            ('D.P.T.Z.', 'D.P.T.Z.'),
            ('D.P.Z.', 'D.P.Z.'),
            ('N.P.T.', 'N.P.T.'),
            ('N.SH.', 'N.SH.'),
            ('N.P.SH.', 'N.P.SH.')
        ], 
        default='Other'
    )

    business_name = TextField('Emri Biznesit')
    owner = TextField('Pronari')
    business_nr = IntegerField('Numri Biznesit')
    fiscal_nr = IntegerField('Numri Fiskal')

    activities = SelectMultipleField('Aktiviteti',
        choices = [
            ('Accomodation', 'Accomodation'),
            ('Restaurant', 'Restaurant'),
            ('Cafe', 'Cafe'),
            ('Museum', 'Museum'),
            ('Sight', 'Sight'),
            ('Art Shop', 'Art Shop'),
            ('Craft Shop', 'Craft Shop'),
            ('Clothing Shop', 'Clothing Shop'),
            ('Shoe Shop', 'Shoe Shop'),
            ('Market', 'Market'),
            ('Bar', 'Bar'),
            ('Nightclub', 'Nightclub'),
            ('Park', 'Park'),
            ('Other', 'Other')
        ]
    )

    # Sector field, and sector C's subfields
    sector_options = [
        'A. Agriculture, Forestry and Fishing', 'B. Mine and Stone quarry (Extraction Industry)',
        'C. Processing Industry', 'D. Supply with power, gas, steam  and conditioner air; water supply',
        'E. Canalization, activities of sewage management and treatment', 'F. Construction',
        'G. Retail sales and wholesale; reparation of motor vehicles and motorcycles', 'H. Transportation and Storage',
        'I. Accommodation and Food service activities', 'J. Information and Communication',
        'K. Financial activities and Insurance', 'L. Real Estate activities',
        'M. Professional, Scientific and Technical activities', 'N. Administrative and supporting services',
        'O. Public Administration and Security – Obligated Social Security', 'P. Education',
        'Q. Human health activities and social works', 'R. Arts, Entertainment and Recreation',
        'S. Other servicing activities',
        'T. Economical household activities as employer; undifferentiated goods and services, economical household activities for own usage',
        'U. Activities of international bodies and organizations'
    ]

    sector_tuple_list = [(x, x) for x in sector_options]
    sector = SelectField('Sektori dhe Pershkrimi', choices=sector_tuple_list)

    sector_c = SelectField(
        "Sektori C",
        choices=[
            ('C1. Wood Industry', 'C1. Wood Industry'),
            ('C2. Food Industry', 'C2. Food Industry'),
            ('C3. Metal Industry', 'C3. Metal Industry'),
            ('C4. Textile Industry', 'C4. Textile Industry'),
            ('C5. Others', 'C5. Others')
        ],
        default='C5. Others'
    )
    business_statute = SelectField(
        'Statuti Bisnesit',
        choices=[('Aktiv', 'Aktiv'), ('Pasiv', 'Pasiv'), ('I pezulluar', 'I pezulluar')]
    )

    registration_date = TextField('Data Regjistrimit')
    phone_nr = TextField('Telefoni')
    email = TextField('E-mail')
    website = TextField('Website')
    facebook = TextField('Facebook')
    twitter = TextField('Twitter')
    address = TextField('Adresa')

    city = SelectField('Qyteti', choices=[('Gjakove', 'Gjakove')], default='Gjakove')

    longitude = FloatField('Longitude')
    latitude = FloatField('Latitude')
    speciality = TextAreaField('Specialiteti i Biznesit')
    other_information = TextAreaField('Pershkrimi')
