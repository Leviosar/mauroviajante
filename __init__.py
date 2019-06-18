import csv
import time
from Classes.Airport import Airport

airports = list()
routes = list()

with open('airports-extended.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row['type'] == 'airport':
            airports.append(Airport(row['airport_name'], row['iata_code'], row['lat'], row['lon']))

with open('routes.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        routes.append(row)

def getAirport(str):
    for airport in airports:
        if airport.code == str:
            return airport
    return None
            
print(getAirport('CWB'))
print(airports[1])
print(len(routes))
