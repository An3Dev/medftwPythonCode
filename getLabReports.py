from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *
from DiagnosticReports import *

def getLabReports(id):
    reports = getDiagnosticReports(id)
    reportNames = []

    for lab, name in reports:
        reportNames.append(name)

    return reportNames

print(getLabReports(2333))