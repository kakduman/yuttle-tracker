import gzip
import pickle
import os

DATA_DIRECTORY = "data/processed_data/arrival_data"

def read_compressed_data(file_path):
    with gzip.open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def add_bus_data(dataset, file_path, predictions_only=False):
    raw_processed_data = read_compressed_data(file_path)
    for raw_processed_datapoint in raw_processed_data:
        if "arrivals" not in raw_processed_datapoint:
            continue

        if None in raw_processed_datapoint["arrivals"].values():
            continue

        if predictions_only:
            clean_datapoint = [
                {int(k): v for k, v in raw_processed_datapoint["estimatedTimes"].items()},
                raw_processed_datapoint["arrivals"] # this is a dictionary containing 32 ground truths!
            ]
        else:
            clean_datapoint = [
                raw_processed_datapoint["pathPercent"],
                raw_processed_datapoint["sinProgress"],
                raw_processed_datapoint["cosProgress"],
                raw_processed_datapoint["lastStop"],
                raw_processed_datapoint["dayPercent"],
                raw_processed_datapoint["weekday"],
                raw_processed_datapoint["arrivals"] # this is a dictionary containing 32 ground truths!
            ]

        dataset.append(clean_datapoint)

def load_dataset(route=1):
    """
    Loads the processed, compressed data for a given route into an array

    Args:
        route (int): The route number to load data for. Defaults to 1 (blue)

    Returns:
        N x d array; d = 7 with the first 6 as inputs and the last column as a dictrionary of ground truths, one for each stop on the route

    """
    dataset = []
    for filename in os.listdir(DATA_DIRECTORY):
        if filename.startswith(f"bus_{route}_") and filename.endswith(".json.gz"):
            file_path = os.path.join(DATA_DIRECTORY, filename)
            if os.path.isfile(file_path):
                add_bus_data(dataset, file_path, predictions_only=False)
    return dataset

def load_estimate_dataset(route=1):
    """
    Loads the official estimated arrival times and the actual arrival times for a given route into an array

    Args:
        route (int): The route number to load data for. Defaults to 1 (blue)

    Returns:
        N x d array; d = 2 with the first column as dictionaries of the estimated arrival times and the second column as dictionaries of the actual arrival times
    """
    dataset = []
    for filename in os.listdir(DATA_DIRECTORY):
        if filename.startswith(f"bus_{route}_") and filename.endswith(".json.gz"):
            file_path = os.path.join(DATA_DIRECTORY, filename)
            if os.path.isfile(file_path):
                add_bus_data(dataset, file_path, predictions_only=True)
    return dataset


if __name__ == '__main__':
    dataset = load_dataset()
    print(dataset[43801])
