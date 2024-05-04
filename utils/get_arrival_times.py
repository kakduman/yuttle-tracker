import os
import gzip
import pickle

MINUTES_IN_BUS_DAY = 660
route_stops = {1: [10, 2, 5, 52, 41, 20, 108, 106, 34, 101, 47, 100, 102, 105, 69, 139, 136, 130, 129, 140, 133, 135, 138, 97, 66, 63, 42, 98, 38, 39, 72, 43]}
arrivals_dict = {}

def is_line_invalid(line):
    # if this occurred on Monday, April 22 (1716350400 - 1716436799), get rid of it because the protests messed up our data
    if 1716350400 <= line["lastUpdate"] <= 1716436799:
        return True
    
    # this is for arrivals after 6pm, which are None
    if type(line['dayPercent']) != float:
        return True
    
    # if we don't know the line's lastStop, get rid of that data point. We're not sure why sometimes they have lastStop = 0...
    if line["lastStop"] == 0:
        return True
    
    return False

def reset_arrivals_dict(arrivals_dict, route):
    for stop in route_stops[route]:
        arrivals_dict[stop] = None


def append_arrival_times(input_file, output_file, route=1):
    '''
    Appends arrival times to a given input file, returning a new file with the arrival times.
    
    Parameters:
    input_file (str): The file to read from.
    output_file (str): The file to write to.
    route (int): The route number of analysis. Defaults to 1 (blue).
    '''
    
    # Function goes in reverse order, finding when the lastStop changed and adding this time to an arrivals dict
    # Then, each line is modified with its corresponding arrival times, and re-reversed
    
    reset_arrivals_dict(arrivals_dict, route)

    with open(input_file, "r") as file:
        prev_stop = None
        unix_time = 99999999999
        updated_lines = []

        lines = file.readlines()
        lines.reverse()
        
        for line in lines:
            # convert raw text to dictionary
            line = eval(line)

            if is_line_invalid(line):
                continue

            # when the date changes (time decreases by MORE than 10800 in one go), reset the arrivals_dict
            unix_time = line["lastUpdate"]
            if line["lastUpdate"] < (unix_time - 10800):
                reset_arrivals_dict(arrivals_dict, route)
            
            if not prev_stop: 
                prev_stop = line["lastStop"]
                continue
            
            # update arrivals_dict if the stop changed
            current_stop = line["lastStop"]
            if current_stop != prev_stop:
                arrivals_dict[current_stop] = line["dayPercent"]
                prev_stop = current_stop
            
            line["arrivals"] = arrivals_dict.copy()

            # transform estimatedTimes to day percentages
            for estimate in line["estimatedTimes"]:
                estimate_in_dayTime = line["estimatedTimes"][estimate] / MINUTES_IN_BUS_DAY
                arrival_estimate = round(estimate_in_dayTime + line["dayPercent"], 5)
                line["estimatedTimes"][estimate] = arrival_estimate
            
            updated_lines.append(line)

        updated_lines.reverse()
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with gzip.open(output_file + '.gz', 'wb') as new_file:
            pickle.dump(updated_lines, new_file)
