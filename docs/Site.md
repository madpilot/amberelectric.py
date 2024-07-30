# Site


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Site Identifier | 
**nmi** | **str** | National Metering Identifier (NMI) for the site | 
**channels** | [**List[Channel]**](Channel.md) | List of channels that are readable from your meter | 
**network** | **str** | The name of the site&#39;s network | 
**status** | [**SiteStatus**](SiteStatus.md) |  | 
**active_from** | **date** | Date the site became active. This date will be in the future for pending sites. It may also be undefined, though if it is, contact [info@amber.com.au](mailto:info@amber.com.au) - there may be an issue with your address. Formatted as a ISO 8601 date when present. | [optional] 
**closed_on** | **date** | Date the site closed. Undefined if the site is pending or active. Formatted as a ISO 8601 date when present. | [optional] 

## Example

```python
from amberelectric.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print Site.to_json()

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_from_dict = Site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


