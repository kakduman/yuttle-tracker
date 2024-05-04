import json
import os
import gzip
import pickle


route_stops = {1: [10, 2, 5, 52, 41, 20, 108, 106, 34, 101, 47, 100, 102, 105, 69, 139, 136, 130, 129, 140, 133, 135, 138, 97, 66, 63, 42, 98, 38, 39, 72, 43]}
arrivals_dict = {}

route_stop_progress = {10: 0.7574379285320636, 2: 0.8100693903319043, 5: 0.8440054213568458, 52: 0.8716423053862119, 41: 0.91, 20: 0.9561084949286741, 108: 0.9760129679929708, 106: 1.0, 34: 0.038237900811054396, 101: 0.05962329244285599, 47: 0.10745151555996796, 100: 0.1328101369610443, 102: 0.1737593212303774, 105: 0.2030971029708586, 69: 0.24730806822917184, 139: 0.2835216542743249, 136: 0.30136998545272076, 130: 0.33057193150829534, 129: 0.35416926058718823, 140: 0.3765943938182113, 133: 0.4042609751799648, 135: 0.42607808057732677, 138: 0.4518605417805998, 97: 0.4856001998816069, 66: 0.5344474411127405, 63: 0.558828997582244, 42: 0.59, 98: 0.6298985138882538, 38: 0.663908526212489, 39: 0.677592282664344, 72: 0.7073775345450428, 43: 0.7346760880904396}

def append_arrival_times(input_file, output_file):
    '''
    Appends arrival times to a given input file, returning a new file with the arrival times.
    
    Parameters:
    input_file (str): The file to read from.
    output_file (str): The file to write to.
    '''
    
    # Function goes in reverse order, finding when the lastStop changed and adding this time to an arrivals dict
    # Then, each line is modified with its corresponding arrival times, and re-reversed
    
    heading = 1 # northbound
    
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
            
            
            # we're actually going to process this point. Might not add it to data, but we need to process it in some way
            unix_time = line["lastUpdate"]
            if 0.62 < line["pathPercent"] < 0.75:
                heading = 1
            elif 0.94 < line["pathPercent"]:
                heading = 0
                
            line["lastStop"] = find_most_recent_stop(line["pathPercent"], heading)
                
            # if we don't know the line's lastStop, get rid of that data point. We're not sure why sometimes they have lastStop = 0...
            if line["lastStop"] == 0:
                continue
            elif line["lastStop"] == 42:
                line["pathPercent"] = 0.59
            elif line["lastStop"] == 41:
                line["pathPercent"] = 0.91
            
            # when the date changes (time decreases by MORE than 10800 in one go), reset the arrivals_dict
            if line["lastUpdate"] < (unix_time - 10800):
                # reset arrivals_dict
                for stop in route_stops[1]:
                    arrivals_dict[stop] = None
                        
            if not previously_recorded_stop:
                previously_recorded_stop = line["lastStop"]
                for estimate in line["estimatedTimes"]:
                    estimate_in_dayTime = line["estimatedTimes"][estimate] / 660
                    try:
                        arrival_estimate = round(estimate_in_dayTime + line["dayPercent"], 5)
                        line["estimatedTimes"][estimate] = arrival_estimate
                        line["arrivals"] = dict(arrivals_dict)
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
        
        # save to a new file .json, make directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with gzip.open(output_file + '.gz', 'wb') as new_file:
            pickle.dump(updated_lines, new_file)

def find_most_recent_stop(path_progress, de_facto_heading):
    '''
    Finds the most recent stop for a given path progress and heading (1 (northbound) or 0 (southbound)).
    
    Returns the stop number.
    '''
    route_stop_progress = {10: 0.7574379285320636, 2: 0.8100693903319043, 5: 0.8440054213568458, 52: 0.8716423053862119, 41: 0.91, 20: 0.9561084949286741, 108: 0.9760129679929708, 106: 1.0, 34: 0.038237900811054396, 101: 0.05962329244285599, 47: 0.10745151555996796, 100: 0.1328101369610443, 102: 0.1737593212303774, 105: 0.2030971029708586, 69: 0.24730806822917184, 139: 0.2835216542743249, 136: 0.30136998545272076, 130: 0.33057193150829534, 129: 0.35416926058718823, 140: 0.3765943938182113, 133: 0.4042609751799648, 135: 0.42607808057732677, 138: 0.4518605417805998, 97: 0.4856001998816069, 66: 0.5344474411127405, 63: 0.558828997582244, 42: 0.5908789960154363, 98: 0.6298985138882538, 38: 0.663908526212489, 39: 0.677592282664344, 72: 0.7073775345450428, 43: 0.7346760880904396}
    # first figure out if de facto heading is 1 or 0 and we're in the sensitive range
    if (0.56 < path_progress < 0.62) or (0.88 < path_progress < 0.94):
        if de_facto_heading == 1:
            path_progress = 0.59
            return 42
        else:
            path_progress = 0.91
            return 41
            
    # then sort dictionary by values, 
    route_stop_progress = dict(sorted(route_stop_progress.items(), key=lambda item: item[1]))
    # print(route_stop_progress)
    
    # then go in order and return first one we're not smaller than by 0.01
    # keeping track of the previous one, so we can return that when we achieve our condition
    prev_stop = 106 # 106 is the largest stop number
    for stop in route_stop_progress:
        if path_progress < route_stop_progress[stop] + 0.008:
            # print(prev_stop)
            return prev_stop
        prev_stop = stop
    raise Exception("No stop found!")
