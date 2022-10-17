from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *

def getMedicationInformation(id):
    medication = getRequest('Medication', f'?patient=Patient/{id}')
    if not medication:
        print("No Medication Found")
        return False

    lst = []
    for med in medication:
        concatenated_string = med['resource']['code']['coding'][0]['display']
        lst.append(concatenated_string)
 
    return lst

[print(r) for r in getMedicationInformation(1)]