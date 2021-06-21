# CurrentIntervalAllOf

Returns the current interval's forecasted price comprised of the weighted average of 5-minute acutal prices and 5-minute forecast prices. In the last 5-minutes of the interval, the price represents the final price for that interval.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimate** | **bool** | Shows true the current price is an estimate. Shows false is the price has been locked in. | 
**type** | **str** |  | [optional]  if omitted the server will use the default value of "CurrentInterval"
**range** | [**Range**](Range.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


