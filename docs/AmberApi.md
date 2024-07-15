# amberelectric.AmberApi

All URIs are relative to *https://api.amber.com.au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_prices**](AmberApi.md#get_current_prices) | **GET** /sites/{siteId}/prices/current | 
[**get_current_renewables**](AmberApi.md#get_current_renewables) | **GET** /state/{state}/renewables/current | 
[**get_prices**](AmberApi.md#get_prices) | **GET** /sites/{siteId}/prices | 
[**get_sites**](AmberApi.md#get_sites) | **GET** /sites | 
[**get_usage**](AmberApi.md#get_usage) | **GET** /sites/{siteId}/usage | 


# **get_current_prices**
> List[Interval] get_current_prices(site_id, next=next, previous=previous, resolution=resolution)



Returns the current price

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import amberelectric
from amberelectric.models.interval import Interval
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
    resolution = 30 # int | Specify the required interval duration resolution. Valid options: 30. Default: 30 (optional) (default to 30)

    try:
        api_response = api_instance.get_current_prices(site_id, next=next, previous=previous, resolution=resolution)
        print("The response of AmberApi->get_current_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmberApi->get_current_prices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site you are fetching prices for. Can be found using the &#x60;/sites&#x60; enpoint | 
 **next** | **int**| Return the _next_ number of forecast intervals | [optional] 
 **previous** | **int**| Return the _previous_ number of actual intervals. | [optional] 
 **resolution** | **int**| Specify the required interval duration resolution. Valid options: 30. Default: 30 | [optional] [default to 30]

### Return type

[**List[Interval]**](Interval.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current price on all channels.&lt;br&gt;&lt;br&gt;Return Order: General &gt; Controlled Load &gt; Feed In.&lt;br&gt;&lt;br&gt;**NOTE**: If a channel is added or removed the index offset will change. It is best to filter or group the array by channel type. |  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  * RateLimit-Policy -  <br>  |
**400** | Bad request |  -  |
**401** | API key is missing or invalid |  -  |
**404** | Site not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_renewables**
> List[Renewable] get_current_renewables(state, next=next, previous=previous, resolution=resolution)



Returns the current percentage of renewables in the grid

### Example

```python
import time
import os
import amberelectric
from amberelectric.models.renewable import Renewable
from amberelectric.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.amber.com.au/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = amberelectric.Configuration(
    host = "https://api.amber.com.au/v1"
)


# Enter a context with an instance of the API client
with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amberelectric.AmberApi(api_client)
    state = 'vic' # str | State you would like the renewables for. Valid states: nsw, sa, qld, vic
    next = 48 # int | Return the _next_ number of forecast intervals (optional)
    previous = 48 # int | Return the _previous_ number of actual intervals. (optional)
    resolution = 30 # int | Specify the required interval duration resolution. Valid options: 5, 30. Default: 30 (optional) (default to 30)

    try:
        api_response = api_instance.get_current_renewables(state, next=next, previous=previous, resolution=resolution)
        print("The response of AmberApi->get_current_renewables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmberApi->get_current_renewables: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| State you would like the renewables for. Valid states: nsw, sa, qld, vic | 
 **next** | **int**| Return the _next_ number of forecast intervals | [optional] 
 **previous** | **int**| Return the _previous_ number of actual intervals. | [optional] 
 **resolution** | **int**| Specify the required interval duration resolution. Valid options: 5, 30. Default: 30 | [optional] [default to 30]

### Return type

[**List[Renewable]**](Renewable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current percentage of renewables in the grid. |  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  * RateLimit-Policy -  <br>  |
**400** | Bad request |  -  |
**404** | State not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices**
> List[Interval] get_prices(site_id, start_date=start_date, end_date=end_date, resolution=resolution)



Returns all the prices between the start and end dates

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import amberelectric
from amberelectric.models.interval import Interval
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
    site_id = '01J23BAP2SFA218BMV8A73Y9Z9' # str | ID of the site you are fetching prices for. Can be found using the `/sites` endpoint
    start_date = '2021-05-05' # date | Return all prices for each interval on and after this day. Defaults to today. (optional)
    end_date = '2021-05-05' # date | Return all prices for each interval on and before this day. Defaults to today. (optional)
    resolution = 30 # int | Specify the required interval duration resolution. Valid options: 5, 30. Default: 30 (optional) (default to 30)

    try:
        api_response = api_instance.get_prices(site_id, start_date=start_date, end_date=end_date, resolution=resolution)
        print("The response of AmberApi->get_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmberApi->get_prices: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site you are fetching prices for. Can be found using the &#x60;/sites&#x60; endpoint | 
 **start_date** | **date**| Return all prices for each interval on and after this day. Defaults to today. | [optional] 
 **end_date** | **date**| Return all prices for each interval on and before this day. Defaults to today. | [optional] 
 **resolution** | **int**| Specify the required interval duration resolution. Valid options: 5, 30. Default: 30 | [optional] [default to 30]

### Return type

[**List[Interval]**](Interval.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of priced intervals&lt;br&gt;&lt;br&gt;Return Order: General &gt; Controlled Load &gt; Feed In.&lt;br&gt;&lt;br&gt;**NOTE**: If a channel is added or removed the index offset will change. It is best to filter or group the array by channel type. |  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  * RateLimit-Policy -  <br>  |
**400** | Bad request |  -  |
**401** | API key is missing or invalid |  -  |
**404** | Site not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites**
> List[Site] get_sites()



Return all sites linked to your account

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import amberelectric
from amberelectric.models.site import Site
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

    try:
        api_response = api_instance.get_sites()
        print("The response of AmberApi->get_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmberApi->get_sites: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Site]**](Site.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sites. |  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  * RateLimit-Policy -  <br>  |
**401** | API key is missing or invalid |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> List[Usage] get_usage(site_id, start_date, end_date, resolution=resolution)



Returns all usage data between the start and end dates. The API can only return 90-days worth of data.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import amberelectric
from amberelectric.models.usage import Usage
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
    site_id = '01J23BAP2SFA218BMV8A73Y9Z9' # str | ID of the site you are fetching usage for. Can be found using the `/sites` enpoint
    start_date = '2021-05-05' # date | Return all usage for each interval on and after this day.
    end_date = '2021-05-05' # date | Return all usage for each interval on and before this day.
    resolution = 30 # int | Specify the required interval duration resolution. Valid options: 30. Default: 30 (optional) (default to 30)

    try:
        api_response = api_instance.get_usage(site_id, start_date, end_date, resolution=resolution)
        print("The response of AmberApi->get_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AmberApi->get_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| ID of the site you are fetching usage for. Can be found using the &#x60;/sites&#x60; enpoint | 
 **start_date** | **date**| Return all usage for each interval on and after this day. | 
 **end_date** | **date**| Return all usage for each interval on and before this day. | 
 **resolution** | **int**| Specify the required interval duration resolution. Valid options: 30. Default: 30 | [optional] [default to 30]

### Return type

[**List[Usage]**](Usage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage for the requested period.&lt;br&gt;&lt;br&gt;Return Order: General &gt; Controlled Load &gt; Feed In.&lt;br&gt;&lt;br&gt;**NOTE**: If a channel is added or removed the index offset will change. It is best to filter or group the array by channel type. |  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  * RateLimit-Policy -  <br>  |
**400** | Bad request |  -  |
**401** | API key is missing or invalid |  -  |
**404** | Site not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

