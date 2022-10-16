from ApiFunctions import *
import pandas as pd

practioners = getRequest('Practitioner')


practionerContacts = []
for practioner in practioners:
    zipcode = practioner['resource']['address'][0]['postalCode']
    if len(zipcode) > 5:
        zipcode = zipcode[0:5]
    elif len(zipcode) < 5:
        while len(zipcode) < 5:
            zipcode = '0' + zipcode
    email = practioner['resource']['telecom'][0]['value']
    practionerContacts.append([zipcode, email])

df = pd.DataFrame(practionerContacts, columns=['Zip Code', 'Email'])
df.to_csv('PractionerContacts', index=False)
