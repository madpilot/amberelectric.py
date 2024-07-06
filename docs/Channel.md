# Channel

Describes a power meter channel.  The General channel provides continuous power - it's the channel all of your appliances and lights are attached to.  Controlled loads are only on for a limited time during the day (usually when the load on the network is low, or generation is high) - you may have your hot water system attached to this channel.  The feed in channel sends power back to the grid - you will have these types of channels if you have solar or batteries.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identifier of the channel | 
**type** | [**ChannelType**](ChannelType.md) |  | 
**tariff** | **str** | The tariff code of the channel | 

## Example

```python
from amberelectric.models.channel import Channel

# TODO update the JSON string below
json = "{}"
# create an instance of Channel from a JSON string
channel_instance = Channel.from_json(json)
# print the JSON string representation of the object
print Channel.to_json()

# convert the object into a dict
channel_dict = channel_instance.to_dict()
# create an instance of Channel from a dict
channel_from_dict = Channel.from_dict(channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


