import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

route_stops = {1: [10, 2, 5, 52, 41, 20, 108, 106, 34, 101, 47, 100, 102, 105, 69, 139, 136, 130, 129, 140, 133, 135, 138, 97, 66, 63, 42, 98, 38, 39, 72, 43]}

# Number of threads for fetching data
MAX_WORKERS = 20

def fetch_data(stop):
    response = requests.get(f'https://yale.downtownerapp.com/routes_eta.php?stop={stop}')
    if response.status_code == 200:
        return response.json()
    else:
        return None



def get_estimated_route_stop_times(route):
    if route not in route_stops:
        raise ValueError(f"Route {route} is not in the route_stops dictionary")
    
    res = []
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_stop = {executor.submit(fetch_data, stop): stop for stop in route_stops[route]}
        
        for future in as_completed(future_to_stop):
            data = future.result()
            if data:
                res.append(str(data) + '\n')
    
    return ''.join(res)

def get_estimated_bus_stop_times(bus_id, estimated_route_stop_times):
    for stop in estimated_route_stop_times:
        if bus_id in stop:
            return stop




if __name__ == "__main__":
    print(get_estimated_route_stop_times(1))
    
    
