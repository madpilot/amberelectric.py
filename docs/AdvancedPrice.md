# AdvancedPrice

Amber has created an advanced forecast system, that represents our confidence in the AEMO forecast. The range indicates where we think the price will land for a given interval.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low** | **float** | The lower bound of our prediction band. Price includes network and market fees. (c/kWh). | 
**high** | **float** | The upper bound of our prediction band. Price includes network and market fees. (c/kWh). | 

## Example

```python
from amberelectric.models.advanced_price import AdvancedPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedPrice from a JSON string
advanced_price_instance = AdvancedPrice.from_json(json)
# print the JSON string representation of the object
print AdvancedPrice.to_json()

# convert the object into a dict
advanced_price_dict = advanced_price_instance.to_dict()
# create an instance of AdvancedPrice from a dict
advanced_price_from_dict = AdvancedPrice.from_dict(advanced_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


