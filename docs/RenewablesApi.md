# amberelectric.RenewablesApi

All URIs are relative to *https://api.amber.com.au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_renewables**](RenewablesApi.md#get_current_renewables) | **GET** /state/{state}/renewables/current | 


# **get_current_renewables**
> List[GetCurrentRenewables200ResponseInner] get_current_renewables(state, next=next, previous=previous, resolution=resolution)



Returns the current percentage of renewables in the grid

### Example


```python
import amberelectric
from amberelectric.models.get_current_renewables200_response_inner import GetCurrentRenewables200ResponseInner
from amberelectric.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.amber.com.au/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = amberelectric.Configuration(
    host = "https://api.amber.com.au/v1"
)


# Enter a context with an instance of the API client
async with amberelectric.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amberelectric.RenewablesApi(api_client)
    state = 'state_example' # str | State you would like the renewables for. Valid states: nsw, sa, qld, vic
    next = 56 # int | Return the _next_ number of forecast intervals (optional)
    previous = 56 # int | Return the _previous_ number of actual intervals. (optional)
    resolution = 30 # int | Specify the required interval duration resolution. Valid options: 5, 30. Default: 30 (optional) (default to 30)

    try:
        api_response = await api_instance.get_current_renewables(state, next=next, previous=previous, resolution=resolution)
        print("The response of RenewablesApi->get_current_renewables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenewablesApi->get_current_renewables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| State you would like the renewables for. Valid states: nsw, sa, qld, vic | 
 **next** | **int**| Return the _next_ number of forecast intervals | [optional] 
 **previous** | **int**| Return the _previous_ number of actual intervals. | [optional] 
 **resolution** | **int**| Specify the required interval duration resolution. Valid options: 5, 30. Default: 30 | [optional] [default to 30]

### Return type

[**List[GetCurrentRenewables200ResponseInner]**](GetCurrentRenewables200ResponseInner.md)

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

