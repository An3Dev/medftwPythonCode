from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *

def getMedicationInformation(id):
    medication = getRequest('Medication', f'?patient=Patient/{id}')
    if not medication:
        print("No Medication Found")
        return False
    print(medication)

    lst = []
    for med in medication:
        concatenatedString = medication = medication['coding']['display']
        lst += concatenatedString
        print(concatenatedString)
    
    return lst