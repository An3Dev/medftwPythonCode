from ApiFunctions import *
import pandas as pd
from geopy import *

practioners = getRequest('Practitioner')

practionerContacts = []
for practioner in practioners:
    PractionerID = practioner['resource']['id']

    zipcode = practioner['resource']['address'][0]['postalCode']
    if len(zipcode) > 5:
        zipcode = zipcode[0:5]
    elif len(zipcode) < 5:
        while len(zipcode) < 5:
            zipcode = '0' + zipcode
    
    email = practioner['resource']['telecom'][0]['value']
    
    location = practioner['resource']['address'][0]
    locationLine = f"{location['line'][0]}, {location['city']}, {location['state']} {zipcode}"

    try:
        locator = Nominatim(user_agent='myGeocoder', timeout=2)
        loc = locator.geocode(locationLine)
    except:
        pass

    try:
        practionerContacts.append([PractionerID, locationLine, loc.latitude, loc.longitude, email])
    except:
        practionerContacts.append([PractionerID, locationLine, '', '', email])
    print(PractionerID)
    

df = pd.DataFrame(practionerContacts, columns=['PractionerID', 'Address', 'Longitude', 'Latitude', 'Email'])
df.to_csv('PractionerContacts.csv', index=False)
