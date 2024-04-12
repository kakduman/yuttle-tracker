import time

from utils.route import Route

# data is being fetched from https://yale.downtownerapp.com/routes_buses.php
WAIT_TIME = 10 # time between fetching data

# Select which routes to track here
blue_line = Route(1)

while True:
    blue_line.record_buses()
    time.sleep(WAIT_TIME)
