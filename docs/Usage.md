# Usage


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
**channel_identifier** | **str** | Meter channel identifier | 
**kwh** | **float** | Number of kWh you consumed or generated. Generated numbers will be negative | 
**quality** | **str** | If the metering company has had trouble contacting your meter, they may make an estimate of your usage for that period. Billable data is data that will appear on your bill. | 
**cost** | **float** | The total cost of your consumption or generation for this period - includes GST | 

## Example

```python
from amberelectric.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print(Usage.to_json())

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_from_dict = Usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


