from flask_wtf import Form
from wtforms import FileField, TextField, TextAreaField


class IndexForm(Form):

    picture = FileField('Fotografia')
    company_name = TextField('Emri Kompanise')
    owner = TextField('Pronari')
    business_nr = TextField('Numri Biznesit')
    fiscal_nr = TextField('Numri Fiskal')
    activity = TextField('Aktiviteti')
    registration_date = TextField('Data Regjistrimit')
    phone_nr = TextField('Telefoni')
    email = TextField('E-mail')
    address = TextAreaField('Adresa')
    other_information = TextAreaField('Informata Tjera')
