#-*- coding: utf-8 -*-
# import this module to recognize non-ASCII characters
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask_wtf import Form
from wtforms import FileField, TextField, TextAreaField, SelectField, IntegerField


class IndexForm(Form):

    sector_options = [
        'A. Agriculture, Forestry and Fishing', 'B. Mine and Stone quarry (Extraction Industry)',
        'C. Processing Industry', 'D. Supply with power, gas, steam  and conditioner air; water supply',
        'E. Canalization, activities of sewage management and treatment', 'F. Construction',
        'G. Retail sales and wholesale; reparation of motor vehicles and motorcycles', 'H. Transportation and Storage',
        'I. Accommodation and Food service activities', 'J.Information and Communication',
        'K. Financial activities and Insurance', 'L. Real Estate activities',
        'M. Professional, Scientific and Technical activities', 'N. Administrative and supporting services',
        'O. Public Administration and Security – Obligated Social Security', 'P. Education',
        'Q. Human health activities and social works', 'R. Arts, Entertainment and Recreation',
        'S. Other servicing activities',
        'T. Economical household activities as employer; undifferentiated goods and services, economical household activities for own usage',
        'U. Activities of international bodies and organizations'
    ]

    sector_tuple_list = [(x, x) for x in sector_options]

    picture = TextField('Fotoja e Kompanise')
    company_name = TextField('Emri Kompanise')
    owner = TextField('Pronari')
    business_nr = IntegerField('Numri Biznesit')
    fiscal_nr = IntegerField('Numri Fiskal')
    activity = TextField('Aktiviteti')
    # Sector field, and sector C's subfields
    sector = SelectField('Sektori dhe Pershkrimi', choices=sector_tuple_list)
    sector_c = SelectField(
        "Sektori C",
        choices=[
            ('C1. Wood Industry', 'C1. Wood Industry'),
            ('C2. Food Industry', 'C2. Food Industry'),
            ('C3. Metal Industry', 'C3. Metal Industry'),
            ('C4. Textile Industry', 'C4. Textile Industry'),
            ('C5. Others', 'C5. Others')
        ]
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
    city = SelectField('Qyteti', choices=[('Gjakove', 'Gjakove')])
    longitude = TextField('Longitude')
    latitude = TextField('Latitude')
    speciality = TextAreaField('Specialiteti i Biznesit')
    other_information = TextAreaField('Pershkrimi')
