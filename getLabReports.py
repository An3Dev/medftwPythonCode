from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *
from DiagnosticReports import *

def getLabReports(id):
    reports = getDiagnosticReports(id)
    reportNames = []

    for lab, name, time in reports:
        date = time[:10]
        reportNames.append([date, name])

    return reportNames[::-1]

[print(r) for r in getLabReports(3536)]