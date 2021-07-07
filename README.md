# Amber - An entirely new way to buy electricity

Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.

Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.

This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

## Details

- API version: 1.0
- Package version: 1.0.0

## Requirements

Python >= 3.6

## Getting started

Not an Amber customer yet? Join here: https://join.amber.com.au/sign-up

Once your account has been created, you need to create an [API token](https://app.amber.com.au/developers)

## Installation

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install amberelectric.py
```

## Usage

### Setup and confirguration

```python
# Import the library
import amberelectric
from amberelectric.api import amber_api

# These are just for demo purposes...
from pprint import pprint
from datetime import date

# Insert the API token you created at https://app.amber.com.au/developers
configuration = amberelectric.Configuration(
    access_token = 'psk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

# Create an API instance
api = amber_api.AmberApi.create(configuration)
```

### Fetching Sites

All the interesting functions require a site id, so find one of those first - they can be identified by the National Metering Identifier (NMI)

```python
try:
    sites = api.get_sites()
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)
```

This will return an List of Sites

### Fetching Prices

The API allows you to fetch previous, current and forecast prices by day.

If no start_date or end_date is supplied, it default to the current day.

Note: If duration is 30, there will be 48 intervals per channel. A duration of
5 returns 288 intervals.

```python
site_id = sites[0].id
try:
    start_date = date(2021, 6, 1)
    end_date = date(2021, 6, 2)
    range = api.get_prices(site_id, start_date=start_date, end_date=end_date)
    today = api.get_prices(site_id)
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)
```

You can also just ask for the current price

```python
site_id = sites[0].id
try:
    current = api.get_current_prices(site_id)
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)
```

and the current price plus some number of previous and next intervals

You can also just ask for the current price

```python
site_id = sites[0].id
try:
    current = api.get_current_price(site_id, next=4)
    # returns the current interval and the next 4 forecast intervasl
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)
```

### Usage

You can request your usage for a given day.

```python
site_id = sites[0].id
try:
    usage = api.get_usage(site_id, date(2021, 6, 1), date(2021, 6, 1))
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)
```
