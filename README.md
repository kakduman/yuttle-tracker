# yuttle-tracker

A better Yuttle tracker, class project for CS 381 (Intro Machine Learning)

## Setup

Create and run the virtual environment with

```bash
python -m venv venv
source venv/bin/activate
pip instal -r requriements.txt
```

In order to get data to train the model, we use `scraper.py`, which records shuttle data every 10 seconds using the API located at `https://yale.downtownerapp.com/routes_buses.php`

First, choose which routes to track at the bottom of `scraper.py` with the code `{route_name} = Route({route number})`

To run the scraper, run `python scraper.py`. It should start populating a `data` folder with a file for every bus you're tracking
