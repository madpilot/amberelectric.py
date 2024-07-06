# Range

When prices are particularly volatile, the API may return a range of NEM spot prices (c/kWh) that are possible.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** | Estimated minimum price (c/kWh) | 
**max** | **float** | Estimated maximum price (c/kWh) | 

## Example

```python
from amberelectric.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print Range.to_json()

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_from_dict = Range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


