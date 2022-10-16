from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *
import pandas as pd
from geopy import distance

def getPractitionerInformation(id):
    name = getNameById(id)
    location = getLocationByName(name)
    print(location[2].split()[-1])
getPractitionerInformation(1)
print(distance())
