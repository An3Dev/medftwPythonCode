from asyncio import run_coroutine_threadsafe
import requests
import base64
from ApiFunctions import *

def getAllergyInformation(id):
    allergyInformation = getRequest('AllergyIntolerance', f'?patient=Patient/{id}')
    if not allergyInformation:
        print('No Allergies Found')
        return False

    allAllergies = []
    i=0
    for allergy in allergyInformation:
        i+=1
        allergyText = allergy['resource']['code']['text'].split('(')[0]
        allAllergies.append(allergy['resource']['code']['text'])
        image = requests.post('https://dev.paint.cohere.ai/txt2img', 
                               json={
                                'prompt': f'{allergyText} ; color', 
                                'H' : 512,
                                'W' : 512,
                                'n_samples' : 1, 
                                'n_iter' : 1})
        imageBytes = base64.b64decode(image.json()['image']) #decode
        f = open(f"Patient {id} Allergy #{i}.png", "wb")
        f.write(imageBytes)

    return allAllergies












