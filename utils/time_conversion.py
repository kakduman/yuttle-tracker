import datetime
import json
import requests

# Example JSON string (replace this with your actual JSON data)
# json_data = '[{"id":21785,"name":"#122","lat":41.297187,"lon":-72.951746,"heading":82,"route":8,"lastStop":59,"lastUpdate":1712930964},{"id":21786,"name":"#329","lat":41.256206,"lon":-72.9903,"heading":287,"route":9,"lastStop":23,"lastUpdate":1712930958},{"id":21787,"name":"#314","lat":41.272138,"lon":-72.972214,"heading":46,"route":10,"lastStop":122,"lastUpdate":1712930962}]'
json_data = requests.get('https://yale.downtownerapp.com/routes_buses.php')

def convert_to_fraction_of_day(unix_time):
    '''
    Convert a UNIX timestamp to a fraction of the day.
    The fraction of the day is the number of seconds since 7 AM divided by the total seconds in the range 7 AM to 6 PM.
    '''
    # Convert UNIX timestamp to a datetime object in UTC
    timestamp_utc = datetime.datetime.utcfromtimestamp(unix_time)
    # print(timestamp_utc)
    # Adjust for Eastern Daylight Time: UTC - 4 hours
    timestamp_edt = timestamp_utc - datetime.timedelta(hours=4)
    
    # Define the start and end times (7 AM to 6 PM EDT)
    start_time = datetime.datetime.combine(timestamp_edt.date(), datetime.time(7, 0))
    end_time = datetime.datetime.combine(timestamp_edt.date(), datetime.time(18, 0))
    
    # Calculate the total seconds in the range 7 AM to 6 PM
    total_seconds = (end_time - start_time).total_seconds()
    # print(total_seconds)
    
    # Calculate the seconds since 7 AM
    seconds_since_start = (timestamp_edt - start_time).total_seconds()
    # print(seconds_since_start)
    
    # Normalize the seconds since 7 AM by the total seconds to get a fraction
    if seconds_since_start < 0 or seconds_since_start > total_seconds:
        # Time is outside the 7 AM to 6 PM range, consider how you want to handle this
        return None
    else:
        fraction_of_day = seconds_since_start / total_seconds
        return round(fraction_of_day, 5)



if __name__ == '__main__':
    bus_data = json.loads(json_data.text)

    # Filter bus data for route 1 and compute fractions of the day
    fractions_of_day = [
        {
            "id": bus["id"],
            "name": bus["name"],
            "fraction_of_day": convert_to_fraction_of_day(bus["lastUpdate"]),
            "real_time": bus["lastUpdate"]
        }
        for bus in bus_data if bus["route"] == 1
    ]

    unix_time = 1712930964
    fraction_of_day = convert_to_fraction_of_day(unix_time)
    if fraction_of_day is not None:
        print(f"Fraction of the day for UNIX timestamp {unix_time}: {fraction_of_day}")
    print('finished')


