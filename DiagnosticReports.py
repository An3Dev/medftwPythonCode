from asyncio import run_coroutine_threadsafe
import requests
from ApiFunctions import *

def getDiagnosticReports(id):
    reports = getRequest('DiagnosticReport', f'?patient=Patient/{id}')
    if not reports:
        print("No Reports Found")
        return False

    lst = []
    for report in reports:
        displays = report['resource']['category'][0]['coding']
        time = report['resource']['effectiveDateTime']
        if len(displays) == 1:
            name = displays[0]['display']
            rep = report['resource']['code']['coding'][0]['display']
            lst.append([name, rep, time])
        """ Implement when data is readable
        if len(displays) == 2:
            print(displays[0]['display'])
            print(report['resource']['presentedForm'][0])
        """
    return lst

[print(r) for r in getDiagnosticReports(1)]
