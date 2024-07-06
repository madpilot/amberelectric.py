# TariffInformation

Information about how your tariff affects an interval

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** | The Time of Use period that is currently active. Only available if the site in on a time of use tariff | [optional] 
**season** | **str** | The Time of Use season that is currently active. Only available if the site in on a time of use tariff | [optional] 
**block** | **float** | The block that is currently active. Only available in the site in on a block tariff | [optional] 
**demand_window** | **bool** | Is this interval currently in the demand window? Only available if the site in on a demand tariff | [optional] 

## Example

```python
from amberelectric.models.tariff_information import TariffInformation

# TODO update the JSON string below
json = "{}"
# create an instance of TariffInformation from a JSON string
tariff_information_instance = TariffInformation.from_json(json)
# print the JSON string representation of the object
print TariffInformation.to_json()

# convert the object into a dict
tariff_information_dict = tariff_information_instance.to_dict()
# create an instance of TariffInformation from a dict
tariff_information_from_dict = TariffInformation.from_dict(tariff_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


