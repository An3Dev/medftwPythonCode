from asyncio import run_coroutine_threadsafe
import requests

from ApiFunctions import *

def getAllergyInformation(id):
    allergyInformation = getRequest('AllergyIntolerance', f'?patient=Patient/{id}')
    if not allergyInformation:
        print('No Allergies Found')
        return []

    allAllergies = []
    i=0
    for allergy in allergyInformation:
        i+=1
        allergyText = allergy['resource']['code']['text'].split('(')[0][:-1]
        allAllergies.append(allergyText)

    return allAllergies














