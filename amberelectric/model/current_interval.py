from typing import Union
from datetime import date, datetime
from .interval import Interval
from .range import Range


class CurrentInterval(Interval):
    range: Union[Range, None]
    """Shows true the current price is an estimate. Shows false is the price has been locked in."""
    estimate: bool

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
        estimate: bool,
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

        self.estimate = estimate
        self.range = kwargs.get('range')

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "type": "CurrentInterval",
            "range": self.range,
            "estimate": self.estimate
        })
        return d
