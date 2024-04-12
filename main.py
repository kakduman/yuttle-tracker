import time
import requests

# https://yale.downtownerapp.com/routes_buses.php

WAIT_TIME = 10 # time between getting data
# record the time (temp), lat/long (temp), route, bus, stop num

class Route:
    def __init__(self, route):
        self.route = route
    
    def record_buses(self):
        response = requests.get('https://yale.downtownerapp.com/routes_buses.php')
        data = response.json()
        filtered_data = [item for item in data if item.get('route') == self.route]

        for bus in filtered_data:
            self.record_bus(bus)
            
    
    def record_bus(self, bus):
        id = bus['id']

        data_dict = {
            "lat": bus["lat"],
            "lon": bus["lon"],
            "lastStop": bus["lastStop"],
            "lastUpdate": bus["lastUpdate"],
        }
        
        with open(f'bus_{self.route}_{id}.txt', 'a') as file:
            file.write(str(data_dict) + '\n')




blue_line = Route(1)

while True:
    blue_line.record_buses()
    time.sleep(WAIT_TIME)

print('finished')
