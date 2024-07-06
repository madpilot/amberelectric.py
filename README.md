# Amber - An entirely new way to buy electricity

Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.

Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.

This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

## Details

- API version: 1.0
- Package version: 2.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Getting started

Not an Amber customer yet? Join here: https://join.amber.com.au/signup

Once your account has been created, you need to create an [API token](https://app.amber.com.au/developers)

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

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import amberelectric
from amberelectric.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = amberelectric.Configuration(
    access_token = 'psk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)


# Enter a context with an instance of the API client
async with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amberelectric.DefaultApi(api_client)
    site_id = 'site_id_example' # str | ID of the site you are fetching prices for. Can be found using the `/sites` enpoint
    next = 56 # int | Return the _next_ number of forecast intervals (optional)
    previous = 56 # int | Return the _previous_ number of actual intervals. (optional)
    resolution = 30 # int | Specify the required interval duration resolution. Valid options: 30. Default: 30 (optional) (default to 30)

    try:
        api_response = await api_instance.get_current_prices(site_id, next=next, previous=previous, resolution=resolution)
        print("The response of DefaultApi->get_current_prices:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_current_prices: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.amber.com.au/v1*

| Class        | Method                                                                  | HTTP request                              | Description |
| ------------ | ----------------------------------------------------------------------- | ----------------------------------------- | ----------- |
| _DefaultApi_ | [**get_current_prices**](docs/DefaultApi.md#get_current_prices)         | **GET** /sites/{siteId}/prices/current    |
| _DefaultApi_ | [**get_current_renewables**](docs/DefaultApi.md#get_current_renewables) | **GET** /state/{state}/renewables/current |
| _DefaultApi_ | [**get_prices**](docs/DefaultApi.md#get_prices)                         | **GET** /sites/{siteId}/prices            |
| _DefaultApi_ | [**get_sites**](docs/DefaultApi.md#get_sites)                           | **GET** /sites                            |
| _DefaultApi_ | [**get_usage**](docs/DefaultApi.md#get_usage)                           | **GET** /sites/{siteId}/usage             |

## Documentation For Models

- [ActualInterval](docs/ActualInterval.md)
- [ActualRenewable](docs/ActualRenewable.md)
- [AdvancedPrice](docs/AdvancedPrice.md)
- [Channel](docs/Channel.md)
- [ChannelType](docs/ChannelType.md)
- [CurrentInterval](docs/CurrentInterval.md)
- [CurrentRenewable](docs/CurrentRenewable.md)
- [ForecastInterval](docs/ForecastInterval.md)
- [ForecastRenewable](docs/ForecastRenewable.md)
- [GetCurrentRenewables200ResponseInner](docs/GetCurrentRenewables200ResponseInner.md)
- [GetPrices200ResponseInner](docs/GetPrices200ResponseInner.md)
- [Interval](docs/Interval.md)
- [PriceDescriptor](docs/PriceDescriptor.md)
- [Range](docs/Range.md)
- [Renewable](docs/Renewable.md)
- [RenewableDescriptor](docs/RenewableDescriptor.md)
- [Site](docs/Site.md)
- [SpikeStatus](docs/SpikeStatus.md)
- [TariffInformation](docs/TariffInformation.md)
- [Usage](docs/Usage.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="apiKey"></a>

### apiKey

- **Type**: Bearer authentication

## Author
