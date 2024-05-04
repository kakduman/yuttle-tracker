import json
import os

route_stops = {1: [10, 2, 5, 52, 41, 20, 108, 106, 34, 101, 47, 100, 102, 105, 69, 139, 136, 130, 129, 140, 133, 135, 138, 97, 66, 63, 42, 98, 38, 39, 72, 43]}
arrivals_dict = {}

def append_arrival_times(input_file, output_file):
    '''
    Appends arrival times to a given input file, returning a new file with the arrival times.
    
    Parameters:
    input_file (str): The file to read from.
    output_file (str): The file to write to.
    '''
    
    # Function goes in reverse order, finding when the lastStop changed and adding this time to an arrivals dict
    # Then, each line is modified with its corresponding arrival times, and re-reversed
    
    for stop in route_stops[1]:
        arrivals_dict[stop] = None

    with open(input_file, "r") as file:
        previously_recorded_stop = None
        # unix_time is infinite
        unix_time = 9999999999
        updated_lines = []
        # reverse the lines
        try:
            lines = file.readlines()
        except Exception as e:
            print(f"Error reading {input_file}: {e}")
            return
        lines.reverse()
        for line in lines:
            # convert raw text to dictionary
            line = eval(line)
            # if this occurred on Monday, April 22 (1716350400 - 1716436799), get rid of it because the protests messed up our data
            if 1716350400 <= line["lastUpdate"] <= 1716436799:
                continue
            # this is for arrivals after 6pm, which are None

            if type(line['dayPercent']) != float:
                continue
            
            # when the date changes (time decreases by MORE than 10800 in one go), reset the arrivals_dict
            if line["lastUpdate"] < (unix_time - 10800):
                # reset arrivals_dict
                for stop in route_stops[1]:
                    arrivals_dict[stop] = None

            # update unix_time
            unix_time = line["lastUpdate"]
            
            if not previously_recorded_stop:
                previously_recorded_stop = line["lastStop"]
                for estimate in line["estimatedTimes"]:
                    estimate_in_dayTime = line["estimatedTimes"][estimate] / 660
                    try:
                        arrival_estimate = round(estimate_in_dayTime + line["dayPercent"], 5)
                        line["estimatedTimes"][estimate] = arrival_estimate
                        updated_lines.append(line)
                    except Exception as e:
                        print(f"Error appending updated lines: {e}")
                        continue
                continue
            current_stop = line["lastStop"]
            if current_stop != previously_recorded_stop:
                # arrivals_dict[current_stop] is set to the previous line's dayPercent
                arrivals_dict[current_stop] = line["dayPercent"]
                previously_recorded_stop = current_stop
            # append arrivals_dict to the line
            # copied because it avoids future changes from affecting it, since dict is mutable
            line["arrivals"] = dict(arrivals_dict)
            for estimate in line["estimatedTimes"]:
                estimate_in_dayTime = line["estimatedTimes"][estimate] / 660
                try:
                    arrival_estimate = round(estimate_in_dayTime + line["dayPercent"], 5)
                    line["estimatedTimes"][estimate] = arrival_estimate
                    updated_lines.append(line)
                except Exception as e:
                    print(f"Error appending updated lines: {e}")
                    continue
            updated_lines.reverse()
        
        # save to a new file as pretty json, make directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w") as new_file:
            json.dump(updated_lines, new_file, indent=4)
            