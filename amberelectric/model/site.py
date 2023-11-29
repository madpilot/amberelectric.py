from datetime import date
from typing import List, Union
from .channel import Channel
from enum import Enum


class SiteStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    CLOSED = "closed"

    @staticmethod
    def from_str(s: Union[str, None]):
        possible = list(filter(lambda t: t.value == s, SiteStatus))
        if len(possible) > 0:
            return possible[0]
        return None


class Site(object):
    def __init__(
        self,
        id: str,
        nmi: str,
        channels: List[Channel],
        network: str,
        status: SiteStatus,
        active_from: Union[date, None],
        closed_on: Union[date, None],
    ):
        self.id = id
        self.nmi = nmi
        self.channels = channels
        self.network = network
        self.status = status
        self.active_from = active_from
        self.closed_on = closed_on

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str(
            {
                "id": self.id,
                "nmi": self.nmi,
                "channels": self.channels,
                "network": self.network,
                "status": self.status,
                "active_from": self.active_from,
                "closed_on": self.closed_on,
            }
        )
