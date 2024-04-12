import json
import requests

# https://yale.downtownerapp.com/routes_buses.php
r = requests.get('https://yale.downtownerapp.com/routes_buses.php')
print(r.text)