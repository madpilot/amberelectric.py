# Renewable


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
from amberelectric.models.renewable import Renewable

# TODO update the JSON string below
json = "{}"
# create an instance of Renewable from a JSON string
renewable_instance = Renewable.from_json(json)
# print the JSON string representation of the object
print(Renewable.to_json())

# convert the object into a dict
renewable_dict = renewable_instance.to_dict()
# create an instance of Renewable from a dict
renewable_from_dict = Renewable.from_dict(renewable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


