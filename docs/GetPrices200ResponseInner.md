# GetPrices200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Length of the interval in minutes. | 
**spot_per_kwh** | **float** | NEM spot price (c/kWh). This is the price generators get paid to generate electricity, and what drives the variable component of your perKwh price - includes GST | 
**per_kwh** | **float** | Number of cents you will pay per kilowatt-hour (c/kWh) - includes GST | 
**var_date** | **date** | Date the interval belongs to (in NEM time). This may be different to the date component of nemTime, as the last interval of the day ends at 12:00 the following day. Formatted as a ISO 8601 date | 
**nem_time** | **datetime** | The interval&#39;s NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time | 
**start_time** | **datetime** | Start time of the interval in UTC. Formatted as a ISO 8601 time | 
**end_time** | **datetime** | End time of the interval in UTC. Formatted as a ISO 8601 time | 
**renewables** | **float** | Percentage of renewables in the grid | 
**channel_type** | [**ChannelType**](ChannelType.md) |  | 
**tariff_information** | [**TariffInformation**](TariffInformation.md) |  | [optional] 
**spike_status** | [**SpikeStatus**](SpikeStatus.md) |  | 
**descriptor** | [**PriceDescriptor**](PriceDescriptor.md) |  | 
**type** | **str** |  | 
**range** | [**Range**](Range.md) |  | [optional] 
**estimate** | **bool** | Shows true the current price is an estimate. Shows false is the price has been locked in. | 

## Example

```python
from amberelectric.models.get_prices200_response_inner import GetPrices200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrices200ResponseInner from a JSON string
get_prices200_response_inner_instance = GetPrices200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPrices200ResponseInner.to_json())

# convert the object into a dict
get_prices200_response_inner_dict = get_prices200_response_inner_instance.to_dict()
# create an instance of GetPrices200ResponseInner from a dict
get_prices200_response_inner_from_dict = GetPrices200ResponseInner.from_dict(get_prices200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


