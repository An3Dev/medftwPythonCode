from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *

def getImmunizationInformation(id):
    immunization = getRequest('Immunization', f'?patient=Patient/{id}')
    if not immunization:
        print("No Immunizations Found")
        return False
    print(immunization)

    lst = []
    for imm in immunization:
        concatenatedString = imm['resource']['vaccineCode']['coding'][0]['display'] + " - " + imm['resource']['meta']['lastUpdated']
        lst += concatenatedString
        print(concatenatedString)
    
    return lst
