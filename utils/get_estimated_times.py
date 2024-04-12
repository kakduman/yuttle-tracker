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
    # Fetch data concurrently. Takes ~1 second instead of ~6 seconds
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_stop = {executor.submit(fetch_data, stop): stop for stop in route_stops[route]}
        for future in as_completed(future_to_stop):
            data = future.result()
            if data:
                res.append(data)
    return res

def get_estimated_bus_stop_times(bus_id, estimated_route_stop_times):
    bus_stop_times = {}
    for stop in estimated_route_stop_times:
        bus_times = next(iter(stop["etas"].values()))['etas']
        stopNum = next(iter(stop["etas"].keys()))
        check = False
        for time in bus_times:
            if time["bus_id"] == bus_id:
                bus_stop_times[stopNum] = time["avg"]
                check = True
        if not check:
            raise ValueError(f"Bus {bus_id} is not in the data at stop {stopNum}")

    # reorder the stops, which are assorted because of the concurrency
    key_order = [str(key) for key in route_stops[1]]
    ordered_times = {key: bus_stop_times[key] for key in key_order if key in bus_stop_times}
    return ordered_times


if __name__ == "__main__":
    stop_times = get_estimated_route_stop_times(1)
    bus_times = get_estimated_bus_stop_times(21800, stop_times)
    print(bus_times)
    
