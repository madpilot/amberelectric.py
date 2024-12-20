# amberelectric
Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.

Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.

This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 2.0.12
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen
For more information, please visit [https://www.amber.com.au](https://www.amber.com.au)

## Requirements.

Python 3.7+

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

### Building

Build via Poetry

```sh
poetry build
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import amberelectric
from amberelectric.rest import ApiException
from pprint import pprint

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
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amberelectric.AmberApi(api_client)
    site_id = '01J23BAP2SFA218BMV8A73Y9Z9' # str | ID of the site you are fetching prices for. Can be found using the `/sites` enpoint
    next = 48 # int | Return the _next_ number of forecast intervals (optional)
    previous = 48 # int | Return the _previous_ number of actual intervals. (optional)
    resolution = 56 # int | Specify the required interval duration resolution. Valid options: 5, 30. Default: Your billing interval length. (optional)

    try:
        api_response = api_instance.get_current_prices(site_id, next=next, previous=previous, resolution=resolution)
        print("The response of AmberApi->get_current_prices:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmberApi->get_current_prices: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.amber.com.au/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AmberApi* | [**get_current_prices**](docs/AmberApi.md#get_current_prices) | **GET** /sites/{siteId}/prices/current | 
*AmberApi* | [**get_current_renewables**](docs/AmberApi.md#get_current_renewables) | **GET** /state/{state}/renewables/current | 
*AmberApi* | [**get_prices**](docs/AmberApi.md#get_prices) | **GET** /sites/{siteId}/prices | 
*AmberApi* | [**get_sites**](docs/AmberApi.md#get_sites) | **GET** /sites | 
*AmberApi* | [**get_usage**](docs/AmberApi.md#get_usage) | **GET** /sites/{siteId}/usage | 


## Documentation For Models

 - [ActualInterval](docs/ActualInterval.md)
 - [ActualRenewable](docs/ActualRenewable.md)
 - [AdvancedPrice](docs/AdvancedPrice.md)
 - [BaseInterval](docs/BaseInterval.md)
 - [BaseRenewable](docs/BaseRenewable.md)
 - [Channel](docs/Channel.md)
 - [ChannelType](docs/ChannelType.md)
 - [CurrentInterval](docs/CurrentInterval.md)
 - [CurrentRenewable](docs/CurrentRenewable.md)
 - [ForecastInterval](docs/ForecastInterval.md)
 - [ForecastRenewable](docs/ForecastRenewable.md)
 - [Interval](docs/Interval.md)
 - [PriceDescriptor](docs/PriceDescriptor.md)
 - [Range](docs/Range.md)
 - [Renewable](docs/Renewable.md)
 - [RenewableDescriptor](docs/RenewableDescriptor.md)
 - [Site](docs/Site.md)
 - [SiteStatus](docs/SiteStatus.md)
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

dev@amber.com.au


