from asyncio import run_coroutine_threadsafe
from sys import getrefcount
from urllib import response
import requests

headers = {
    'x-api-key': 'SJ8YzDQlJS94hddGrJ0FY1Wt4aVq1B1T2DlLHigi',
}

postHeaders = {
    'accept': '*/*',
    'x-api-key': 'SJ8YzDQlJS94hddGrJ0FY1Wt4aVq1B1T2DlLHigi',
    'Content-Type': 'application/fhir+json',
}
ourLink = "https://fhir.sz5jd1jcumq1.static-test-account.isccloud.io/"
# https://portal.events.isccloud.io/deployments/sz5jd1jcumq1/overview

def executePost(resource, json):
    requests.post(f'{ourLink}{resource}', headers=postHeaders, json=json)



def getRequest(resource="", att="", numPages=False):
    response = requests.get(f'{ourLink}{resource}{att}', headers=headers, verify=True)
    if not response:
        print('Resource not Found')
        return False
    data = response.json()
    if str(data['resourceType']) == 'Bundle':
        pages = -(data['total']//-100)
        if numPages:
            if numPages > pages:
                print('Asked for too many pages, returning all pages')
            else:
                pages = numPages
        print(f'Loading {pages} page(s)')
        if pages == 0:
            print('No Data Found')
            return False
        elif pages == 1:
            print("1 page entry")
            return response.json()['entry']

        baseLink = data['link'][0]['url']
        before = baseLink[:baseLink.index('page=')+5] 
        after = baseLink[baseLink.index('page=')+6:] 

        entries = []
        for pageNum in range(1, pages+1):
            print(f'Loading page {pageNum}')
            thisPageData = requests.get(f'{before}{pageNum}{after}', headers=headers, verify=True).json()
            entries += thisPageData['entry']

        return entries
    else:
        return data
   
def getPatientIds():
    patientIds = []
    PatientResponse = getRequest('Patient')
    for patient in PatientResponse:
        patientIds.append(patient['resource']['id'])
    return patientIds

def getPatientByName(name):
    patient = getRequest('Patient', f'?name={name}')
    if not patient:
        print('Patient Not Found')
        return False
    if len(patient) > 1:
        print(f'Returning first of {len(patient)} patients found')
        return patient[0]
    return patient[0]

def getPatientById(id):
    return getRequest('Patient', f'/{id}')

def getNameById(id):
    return getPatientById(id)['name'][0]['given'][0]

def getCleanNameById(id):
    pureName = getNameById(id)
    numbers = '0987654321'
    name = ''.join([c for c in pureName if c not in numbers])
    return name

def getCleanNameByName(pureName):
    numbers = '0987654321'
    name = ''.join([c for c in pureName if c not in numbers])
    return name

def getIdByName(name):
    return getPatientByName(name)['resource']['id']

def getLocationByName(name):
    patient = getPatientByName(name)
    if patient:
        location = patient['resource']['address'][0]
        locationLL = location['extension'][0]['extension']
        locationLine = f"{location.get('line', '')[0]}, {location.get('city', '')}, {location.get('state', '')} {location.get('postalCode', '')}"
        return (locationLL[0]['valueDecimal'], locationLL[1]['valueDecimal'], locationLine)

def getLocationById(id):
    patient = getPatientById(id)
    if patient:
        location = patient['address'][0]
        locationLL = location['extension'][0]['extension']
        locationLine = f"{location.get('line', '')[0]}, {location.get('city', '')}, {location.get('state', '')} {location.get('postalCode', '')}"
        return (locationLL[0]['valueDecimal'], locationLL[1]['valueDecimal'], locationLine)

def getPractionerNameById(id):
    practitioner = getRequest('Practitioner', f'/{id}')
    names = practitioner['name'][0]
    return f"{names['prefix'][0]}{names['given'][0]} {names['family']}"
