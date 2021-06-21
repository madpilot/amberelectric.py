from enum import Enum


class ChannelType(Enum):
    GENERAL = "general"
    CONTROLLED_LOAD = "controlledLoad"
    FEED_IN = "feedIn"


class Channel(object):
    def __init__(self, identifier: str, type: ChannelType):
        self.identifier = identifier
        self.type = type

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str({'identifier': self.identifier, 'type': self.type})
