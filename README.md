# amberelectric

Python interface to the Amber Electric Public API: https://app.amber.com.au/developers

- API version: 1.0
- Package version: 1.0.0

## Requirements.

Python >= 3.6

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import amberelectric
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import amberelectric
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import amberelectric
from pprint import pprint
from amberelectric.api import amber_api
from amberelectric.model.current_interval import CurrentInterval
from amberelectric.model.site import Site
from amberelectric.model.usage import Usage
# Defining the host is optional and defaults to https://api.amber.com.au/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = amberelectric.Configuration(
    host = "https://api.amber.com.au/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = amberelectric.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

api = amber_api.AmberApi.create(configuration)
try:
    sites = api.get_sites()
except amberelectric.ApiException as e:
    print("Exception: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.amber.com.au/v1*

| Class      | Method                                       | HTTP request                           | Description                        |
| ---------- | -------------------------------------------- | -------------------------------------- | ---------------------------------- |
| _AmberApi_ | **get_sites**                                | **GET** /sites                         | Returns all sites                  |
| _AmberApi_ | **get_prices(site_id)**                      | **GET** /sites/{siteId}/prices/current | Returns all prices for the site    |
| _AmberApi_ | **get_current_prices(site_id)**              | **GET** /sites/{siteId}/prices         | Returns current price for the site |
| _AmberApi_ | **get_usage(site_id, start_date, end_date)** | **GET** /sites/{siteId}/usage          | Returns usage for the site         |

## Documentation For Authorization

## apiKey

- **Type**: Bearer authentication

### To generate

Visit [the developer area](https://app.amber.com.au/developers) and click _Generate an API Token_

## Author

Myles Eftos
