# yuttle-tracker

A better Yuttle tracker, class project for CS 381 (Intro Machine Learning)

## Setup

Create and run the virtual environment with

```bash
python -m venv venv
source venv/bin/activate
pip instal -r requriements.txt
```

## Collecting Data

In order to get data to train the model, we use `scraper.py`, which records shuttle data every 10 seconds using the API located at `https://yale.downtownerapp.com/routes_buses.php`

First, choose which routes to track at the bottom of `scraper.py` with the code `{route_name} = Route({route number})`. By default it is just the blue line. Check the `utils/route_stops.txt` file to see which routes are already set up. If a route is not set up, go to `https://yale.downtownerapp.com/text/routes/{route_num}` and manually write down every stop number in an array and then put the array into the `route_stops` dictionary in `utils/get_estimated_times.py`

To run the scraper, run `python scraper.py`. It should start populating a `data` folder with a file for every bus you're tracking.

We ran the scraper for 2 weeks using a remote server. The buses only run from 7 AM - 6 PM, and only run on their standard route on Mon - Fri.

## Procesing the Data

Once the data is collected and residing in the folder `data/raw_data`, we need to make some adjustments. Some of the raw data we collected is useless, and we throw it out. In addition, the `lastStop` value from DowntownerApp is innacurate, so we must calculate it ourselves.

To process the data, run `python post-processing.py` It should create a new folder, `data/processed_data/arrival_data`, which is the data we actually want.

Note that the processed data is converted to binary and then compressed to save storage, as in the 3 weeks that we ran the scraper for, it ended up creating well 85 MB of data in the raw data, which converts to about 150 MB in uncompressed processed data.

## Training the model

Finally, with processed data, you can train the machine learning model. We created two types of models: a linear regression model and a neural network.

To create and train the model, simply walk through the code blocks in `main.ipynb`
