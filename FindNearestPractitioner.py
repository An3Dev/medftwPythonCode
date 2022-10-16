import pandas as pd
from ApiFunctions import *
from geopy import distance

df = pd.read_csv('PractionerContacts.csv')

def getDistance(lat1, lon1, lat2, lon2):
    if any([pd.isnull(lat1), pd.isnull(lat2)]):
        return float('inf')
    else:
        coord1 = (lat1, lon1)
        coord2 = (lat2, lon2)
        return distance.distance(coord1, coord2).miles


def getNearestPractitioner(id):
    location = getLocationById(id)
    df['Distance'] = df.apply(lambda x: getDistance(x.Longitude, x.Latitude, location[0], location[1]), axis=1)
    closestPractioners = df.nsmallest(3, 'Distance')

    closest = []
    for i in closestPractioners.index:
        p = df.iloc[i]
        closest.append([getCleanNameByName(getPractionerNameById(p['PractionerID'])), 
                        p['Email'], 
                        p['Address'], 
                        p['Distance']])
    return closest





