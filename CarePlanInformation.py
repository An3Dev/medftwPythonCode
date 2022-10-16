from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *

def getCarePlanInformation(id):
    carePlans = getRequest('CarePlan', f'?subject=Patient/{id}')
    """
    plans = []
    if not carePlans:
        print("No Care Plan Found")
        return False
    for carePlan in carePlans:
        s = carePlan['resource']['text']['div']
        strings = []
        s = s.split('>')
        for st in s:
            if st[:1] != '<' and st[:1]:
                strings.append(st.split('<')[0])
        care = [strings[0],
                strings[2],
                strings[4]
                ]
        plans.append(care)
    
    return plans
    """
    if carePlans:
        plans = []
        for care in carePlans:
            text = care['resource']['text']['div']
            if 'Activities' in text:
                s = text.split('>')
                strings = []
                for st in s:
                    if st[:1] != '<' and st[:1]:
                        strings.append(st.split('<')[0])
                
                care = []
                try:
                    care.append(strings[0])
                except:
                    pass
                try:
                    care.append(strings[2])
                except:
                    pass
                try:
                    care.append(strings[4])
                except:
                    pass

                plans.append(care)
        return plans
    else:
        return []

print(getCarePlanInformation(1))