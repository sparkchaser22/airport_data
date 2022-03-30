# Yilmaz A.
# 3.30.2022

import json
from collections import defaultdict
from Airport import Airport

airport_data_file = "airports.geojson"

def airports_list(datafile):
    with open(datafile) as file:
            data = json.load(file)

    airports = []

    for d in data['features']:
        airport_id = d['properties']['ICAO_ID']
        name = d['properties']['NAME']
        country = d['properties']['COUNTRY']
        state = d['properties']['STATE']
        
        airport = Airport(airport_id, name, country, state)
        airports.append(airport)

    return airports

def airports_dict(datafile):

    with open(datafile) as file:
            data = json.load(file)

    airports_dict = defaultdict(None)

    for d in data['features']:
        airport_id = d['properties']['ICAO_ID']
        name = d['properties']['NAME']
        country = d['properties']['COUNTRY']
        state = d['properties']['STATE']
        airport = Airport(airport_id, name, country, state)
        
        airports_dict[airport_id] = airport

    return airports_dict


listAirports = airports_list(airport_data_file)
dictAirports = airports_dict(airport_data_file)
print(listAirports[0])
print(dictAirports['KAUS'])

