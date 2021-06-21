from typing import List
from .channel import Channel


class TariffInformation(object):
    def __init__(self, id: str, nmi: str, channels: List[Channel]):
        self.id = id
        self.nmi = nmi
        self.channels = channels
