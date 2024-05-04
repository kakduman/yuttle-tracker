import gzip
import pickle

def read_compressed_data(file_path):
    with gzip.open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data