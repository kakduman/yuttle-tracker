from utils.get_arrival_times import append_arrival_times
import os

# go through every file in the data directory and run append_arrival_times on it, saving it as .json instead of .txt
for file in os.listdir('data/raw_data'):
    append_arrival_times(f'data/raw_data/{file}', f'data/processed_data/arrival_data/{file[:-4]}.json')