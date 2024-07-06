# GetCurrentRenewables200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**duration** | **int** | Length of the interval in minutes. | 
**var_date** | **date** | Date the interval belongs to (in NEM time). This may be different to the date component of nemTime, as the last interval of the day ends at 12:00 the following day. Formatted as a ISO 8601 date | 
**nem_time** | **datetime** | The interval&#39;s NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time | 
**start_time** | **datetime** | Start time of the interval in UTC. Formatted as a ISO 8601 time | 
**end_time** | **datetime** | End time of the interval in UTC. Formatted as a ISO 8601 time | 
**renewables** | **float** | Percentage of renewables in the grid | 
**descriptor** | [**RenewableDescriptor**](RenewableDescriptor.md) |  | 

## Example

```python
from amberelectric.models.get_current_renewables200_response_inner import GetCurrentRenewables200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrentRenewables200ResponseInner from a JSON string
get_current_renewables200_response_inner_instance = GetCurrentRenewables200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetCurrentRenewables200ResponseInner.to_json())

# convert the object into a dict
get_current_renewables200_response_inner_dict = get_current_renewables200_response_inner_instance.to_dict()
# create an instance of GetCurrentRenewables200ResponseInner from a dict
get_current_renewables200_response_inner_from_dict = GetCurrentRenewables200ResponseInner.from_dict(get_current_renewables200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


