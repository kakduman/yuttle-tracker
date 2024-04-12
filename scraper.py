import time
import requests
import os

from utils.path_conversion import find_progress
from utils.time_conversion import convert_to_fraction_of_day

# data is being fetched from https://yale.downtownerapp.com/routes_buses.php

WAIT_TIME = 10 # time between getting data

class Route:
    def __init__(self, route):
        self.route = route
        os.makedirs('./data', exist_ok=True)
    
    def record_buses(self):
        response = requests.get('https://yale.downtownerapp.com/routes_buses.php')
        data = response.json()
        filtered_data = [item for item in data if item.get('route') == self.route]

        for bus in filtered_data:
            self.record_bus(bus)
            
    def record_bus(self, bus):
        id = bus['id']
        if bus["lastUpdate"] is None:
            return
        
        progress, _ = find_progress(bus["lat"], bus["lon"])

        data_dict = {
            "lat": bus["lat"],
            "lon": bus["lon"],
            "pathPercent": progress,
            "lastStop": bus["lastStop"],
            "lastUpdate": bus["lastUpdate"],
            "dayPercent": convert_to_fraction_of_day(bus["lastUpdate"])
        }
        
        with open(f'data/bus_{self.route}_{id}.txt', 'a') as file:
            file.write(str(data_dict) + '\n')


# Select which routes to track here
blue_line = Route(1)

while True:
    blue_line.record_buses()
    time.sleep(WAIT_TIME)