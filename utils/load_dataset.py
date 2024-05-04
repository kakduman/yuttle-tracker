__all__ = ["load_dataset"]

import gzip
import pickle
import os

DATA_DIRECTORY = "data/processed_data/arrival_data"

def read_compressed_data(file_path):
    with gzip.open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def add_bus_data(dataset, file_path):
    raw_processed_data = read_compressed_data(file_path)
    for raw_processed_datapoint in raw_processed_data:
        clean_datapoint = [
            raw_processed_datapoint["pathPercent"],
            raw_processed_datapoint["sinProgress"],
            raw_processed_datapoint["cosProgress"],
            raw_processed_datapoint["lastStop"],
            raw_processed_datapoint["dayPercent"],
            raw_processed_datapoint["weekday"],
            raw_processed_datapoint["estimatedTimes"] # this is a dictionary containing 32 ground truths!
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
                add_bus_data(dataset, file_path)
    return dataset


if __name__ == '__main__':
    dataset = load_dataset()
    print(dataset[0])
