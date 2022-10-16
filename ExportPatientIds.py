from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *


with open('PatientIds.txt', 'x') as f:
    f.write(str(getPatientIds()))


