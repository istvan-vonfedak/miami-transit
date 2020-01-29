# Dependencies
#  pip install requests

import requests
import json

response = requests.get('http://miami-transit-api.herokuapp.com/api/TrainStations.json')

if response.status_code == 404:
    print('Not Found.')
    exit()

if response.status_code == 200:
    print('Success!')

stations = response.json()['RecordSet']['Record']

def printStations():
    i = 0
    while i < len(stations):
        print(stations[i]['Station'], end=', ')
        print(stations[i]['StationID'])
        i+=1

def printTrainSchedules(StationID):
    schedules = requests.get('https://miami-transit-api.herokuapp.com/api/TrainTracker.json?StationID=' + StationID).json()['RecordSet']['Record']
    if response.status_code == 404:
        print('Not Found.')
        exit()
    print('\nNorth Bound Trains')
    print(schedules['NB_Time1'], schedules['NB_Time1_LineID'])
    print(schedules['NB_Time2'], schedules['NB_Time2_LineID'])
    print(schedules['NB_Time3'], schedules['NB_Time3_LineID'])

    print('\nSouth Bound Trains')
    print(schedules['SB_Time1'], schedules['NB_Time1_LineID'])
    print(schedules['SB_Time2'], schedules['NB_Time2_LineID'])
    print(schedules['SB_Time3'], schedules['NB_Time3_LineID'])

printStations()

printTrainSchedules('BLK')

# print(len(stations))
