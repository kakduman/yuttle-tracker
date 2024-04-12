import requests
import os
from math import sin, cos, pi

from utils.path_conversion import find_progress
from utils.time_conversion import convert_to_fraction_of_day, get_weekday
from utils.get_estimated_times import get_estimated_bus_stop_times, get_estimated_route_stop_times


class Route:
    def __init__(self, route):
        self.route = route
        os.makedirs('./data/live_data', exist_ok=True)
    
    def record_buses(self):
        response = requests.get('https://yale.downtownerapp.com/routes_buses.php')
        data = response.json()
        filtered_data = [item for item in data if item.get('route') == self.route]
        estimated_route_stop_times = get_estimated_route_stop_times(self.route)

        for bus in filtered_data:
            self.record_bus(bus, estimated_route_stop_times)
            
    def record_bus(self, bus, estimated_route_stop_times):
        name = bus['name'][1:]
        unix_time = bus["lastUpdate"]

        if unix_time == None or get_weekday(unix_time) > 4:
            return
        
        progress, _ = find_progress(bus["lat"], bus["lon"])

        data_dict = {
            "lat": bus["lat"],
            "lon": bus["lon"],
            "pathPercent": progress,
            "sinProgress": sin(2 * pi * progress),
            "cosProgress": cos(2 * pi * progress),
            "lastStop": bus["lastStop"],
            "lastUpdate": bus["lastUpdate"],
            "dayPercent": convert_to_fraction_of_day(bus["lastUpdate"]),
            "weekday": get_weekday(bus["lastUpdate"]),
            "estimatedTimes": get_estimated_bus_stop_times(name, estimated_route_stop_times)
        }
        
        with open(f'data/live_data/bus_{self.route}_{name}.txt', 'a') as file:
            file.write(str(data_dict) + '\n')