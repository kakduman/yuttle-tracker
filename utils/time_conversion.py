import datetime
import json
import requests
import pytz

json_data = requests.get('https://yale.downtownerapp.com/routes_buses.php')

def convert_to_fraction_of_day(unix_time):
    '''
    Convert a UNIX timestamp to a fraction of the day.
    The fraction of the day is the number of seconds since 7 AM divided by the total seconds in the range 7 AM to 6 PM.
    
    Parameters:
    unix_time (int): The UNIX timestamp to convert.
    
    Returns:
    float: The fraction of the day, or None if the UNIX timestamp is outside the range 7 AM to 6 PM.
    '''
    # Convert UNIX timestamp to a datetime object in UTC
    edt = pytz.timezone('America/New_York')
    current_time_edt = datetime.datetime.now(pytz.utc).astimezone(edt)
    
    # Define the start and end times (7 AM to 6 PM EDT)
    start_time = datetime.datetime.combine(current_time_edt.date(), datetime.time(7, 0)).astimezone(edt)
    end_time = datetime.datetime.combine(current_time_edt.date(), datetime.time(18, 0)).astimezone(edt)
    
    # Calculate the total seconds in the range 7 AM to 6 PM
    total_seconds = (end_time - start_time).total_seconds()
    # print(total_seconds)
    
    # Calculate the seconds since 7 AM
    seconds_since_start = (current_time_edt - start_time).total_seconds()
    # print(seconds_since_start)
    
    # Normalize the seconds since 7 AM by the total seconds to get a fraction
    if seconds_since_start < 0 or seconds_since_start > total_seconds:
        # Time is outside the 7 AM to 6 PM range
        return None
    else:
        fraction_of_day = seconds_since_start / total_seconds
        return round(fraction_of_day, 5)

def get_weekday(unix_time):
    '''
    Convert a UNIX timestamp to a weekday.
    
    Parameters:
    unix_time (int): The UNIX timestamp to convert.
    
    Returns:
    int: The weekday as an integer, where Monday is 0 and Sunday is 6.
    '''
    edt = pytz.timezone('America/New_York')
    current_time_edt = datetime.datetime.now(pytz.utc).astimezone(edt)
    weekday = current_time_edt.weekday()
    return weekday




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
    print(get_weekday(unix_time))
    print('finished')


