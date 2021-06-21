# ActualInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **float** | Length of the interval in minutes. | 
**spot_per_kwh** | **float** | NEM spot price. This is the price generators get paid to generate electricity, and what drives the variable component of your perKwh price | 
**per_kwh** | **float** | Number of cents you will pay per kilowatt-hour (c/kWh) | 
**date** | **date** | Date the interval belongs to. This may be different to the date component of nemTime, as the last interval of the day ends at 12:30 the following day. Formatted as a ISO 8601 date | 
**nem_time** | **datetime** | The interval&#39;s NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time | 
**start_time** | **datetime** | Start time of the interval in UTC. Formatted as a ISO 8601 time | 
**end_time** | **datetime** | End time of the interval in UTC. Formatted as a ISO 8601 time | 
**renewables** | **float** | Percentage of renewables in the grid | 
**channel_type** | **str** | Meter channel type | 
**spike_status** | **str** | Indicates whether this interval will potentially spike, or is currently in a spike state | 
**type** | **str** |  | defaults to "ActualInterval"
**tariff_information** | **TariffInformation** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


