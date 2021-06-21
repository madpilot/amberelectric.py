from typing import List
from .channel import Channel


class Site(object):
    def __init__(self, id: str, nmi: str, channels: List[Channel]):
        self.id = id
        self.nmi = nmi
        self.channels = channels

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str({'id': self.id, 'nmi': self.nmi, 'channels': self.channels})
