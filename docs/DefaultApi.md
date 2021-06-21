# amberelectric.DefaultApi

All URIs are relative to *https://api.amber.com.au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_get**](DefaultApi.md#sites_get) | **GET** /sites | 
[**sites_site_id_prices_current_get**](DefaultApi.md#sites_site_id_prices_current_get) | **GET** /sites/{siteId}/prices/current | 
[**sites_site_id_prices_get**](DefaultApi.md#sites_site_id_prices_get) | **GET** /sites/{siteId}/prices | 
[**sites_site_id_usage_get**](DefaultApi.md#sites_site_id_usage_get) | **GET** /sites/{siteId}/usage | 


# **sites_get**
> [Site] sites_get()



Return all sites linked to your account

### Example

* Bearer Authentication (apiKey):
```python
import time
import amberelectric
from amberelectric.api import default_api
from amberelectric.model.site import Site
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.sites_get()
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Site]**](Site.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sites. |  -  |
**401** | API key is missing or invalid |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_prices_current_get**
> [CurrentInterval] sites_site_id_prices_current_get(site_id)



Returns the current price

### Example

* Bearer Authentication (apiKey):
```python
import time
import amberelectric
from amberelectric.api import default_api
from amberelectric.model.current_interval import CurrentInterval
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    site_id = "siteId_example" # str | ID of the site you are fetching prices for. Can be found using the `/sites` enpoint
    resolution = 30 # float | Specify the required interval duration resolution. Valid options: 30. Default: 30 (optional) if omitted the server will use the default value of 30

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sites_site_id_prices_current_get(site_id)
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_site_id_prices_current_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sites_site_id_prices_current_get(site_id, resolution=resolution)
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_site_id_prices_current_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site you are fetching prices for. Can be found using the &#x60;/sites&#x60; enpoint |
 **resolution** | **float**| Specify the required interval duration resolution. Valid options: 30. Default: 30 | [optional] if omitted the server will use the default value of 30

### Return type

[**[CurrentInterval]**](CurrentInterval.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current price on all channels |  -  |
**400** | Bad request |  -  |
**401** | API key is missing or invalid |  -  |
**404** | Site not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_prices_get**
> [object] sites_site_id_prices_get(site_id)



Returns all the prices between the start and end dates

### Example

* Bearer Authentication (apiKey):
```python
import time
import amberelectric
from amberelectric.api import default_api
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    site_id = "siteId_example" # str | ID of the site you are fetching prices for. Can be found using the `/sites` enpoint
    start_date = None # bool, date, datetime, dict, float, int, list, str, none_type | Return all prices for each interval on and after this day. Defaults to today. (optional)
    end_date = None # bool, date, datetime, dict, float, int, list, str, none_type | Return all prices for each interval on and before this day. Defaults to today. (optional)
    resolution = 30 # float | Specify the required interval duration resolution. Valid options: 30. Default: 30 (optional) if omitted the server will use the default value of 30

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sites_site_id_prices_get(site_id)
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_site_id_prices_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sites_site_id_prices_get(site_id, start_date=start_date, end_date=end_date, resolution=resolution)
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_site_id_prices_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site you are fetching prices for. Can be found using the &#x60;/sites&#x60; enpoint |
 **start_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| Return all prices for each interval on and after this day. Defaults to today. | [optional]
 **end_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| Return all prices for each interval on and before this day. Defaults to today. | [optional]
 **resolution** | **float**| Specify the required interval duration resolution. Valid options: 30. Default: 30 | [optional] if omitted the server will use the default value of 30

### Return type

**[object]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of priced intervals |  -  |
**400** | Bad request |  -  |
**401** | API key is missing or invalid |  -  |
**404** | Site not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_usage_get**
> [Usage] sites_site_id_usage_get(site_id, start_date, end_date)



Returns all usage data between the start and end dates

### Example

* Bearer Authentication (apiKey):
```python
import time
import amberelectric
from amberelectric.api import default_api
from amberelectric.model.usage import Usage
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    site_id = "siteId_example" # str | ID of the site you are fetching usage for. Can be found using the `/sites` enpoint
    start_date = None # bool, date, datetime, dict, float, int, list, str, none_type | Return all usage for each interval on and after this day.
    end_date = None # bool, date, datetime, dict, float, int, list, str, none_type | Return all usage for each interval on and before this day.
    resolution = 30 # float | Specify the required interval duration resolution. Valid options: 30. Default: 30 (optional) if omitted the server will use the default value of 30

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sites_site_id_usage_get(site_id, start_date, end_date)
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_site_id_usage_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sites_site_id_usage_get(site_id, start_date, end_date, resolution=resolution)
        pprint(api_response)
    except amberelectric.ApiException as e:
        print("Exception when calling DefaultApi->sites_site_id_usage_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site you are fetching usage for. Can be found using the &#x60;/sites&#x60; enpoint |
 **start_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| Return all usage for each interval on and after this day. |
 **end_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| Return all usage for each interval on and before this day. |
 **resolution** | **float**| Specify the required interval duration resolution. Valid options: 30. Default: 30 | [optional] if omitted the server will use the default value of 30

### Return type

[**[Usage]**](Usage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage for the requested period |  -  |
**401** | API key is missing or invalid |  -  |
**400** | Bad request |  -  |
**404** | Site not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

