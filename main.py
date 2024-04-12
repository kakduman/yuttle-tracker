import time
import requests

# https://yale.downtownerapp.com/routes_buses.php

WAIT_TIME = 10 # time between getting data

with open('data.txt', 'a') as file:
    while True:
        r = requests.get('https://yale.downtownerapp.com/routes_buses.php')
        file.write(f'{r.text}\n')
        print('wrote data')
        time.sleep(WAIT_TIME)

print('finished')
