from typing import Union
from datetime import date, datetime
from .interval import Interval
from .range import Range


class Usage(Interval):
    channelIdentifier: str
    kwh: float
    quality: str
    cost: float

    def __init__(
        self,
        duration: float,
        spot_per_kwh: float,
        per_kwh: float,
        date: date,
        nem_time: datetime,
        start_time: datetime,
        end_time: datetime,
        renewables: float,
        channel_type: str,
        spike_status: str,
        channelIdentifier: str,
        kwh: float,
        quality: str,
        cost: float,
        **kwargs
    ):
        super().__init__(
            duration,
            spot_per_kwh,
            per_kwh,
            date,
            nem_time,
            start_time,
            end_time,
            renewables,
            channel_type,
            spike_status,
            **kwargs)

        self.channelIdentifier = channelIdentifier
        self.kwh = kwh
        self.quality = quality
        self.cost = cost

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "type": "Usage",
            "channelIdentifier": self.channelIdentifier,
            "kwh": self.kwh,
            "quality": self.quality,
            "cost": self.cost
        })
        return d
