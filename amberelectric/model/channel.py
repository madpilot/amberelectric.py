from enum import Enum
from typing import Union


class ChannelType(Enum):
    GENERAL = "general"
    CONTROLLED_LOAD = "controlledLoad"
    FEED_IN = "feedIn"

    def from_str(s: Union[str, None]):
        possible = list(filter(lambda t: t.value == s, ChannelType))
        if len(possible) > 0:
            return possible[0]


class Channel(object):
    """Describes a power meter channel.

    The General channel provides continuous power - it's the channel all of your appliances and lights are attached to.

    Controlled loads are only on for a limited time during the day (usually when the load on the network is low, or generation is high) - you may have your hot water system attached to this channel.

    The feed in channel sends power back to the grid - you will have these types of channels if you have solar or batteries."""

    """Identifier of the channel"""
    identifier: str

    """Channel type."""
    type: ChannelType

    def __init__(self, identifier: str, type: ChannelType):
        self.identifier = identifier
        self.type = ChannelType.from_str(type)

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str({'identifier': self.identifier, 'type': self.type})
