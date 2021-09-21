from .interval import Interval
from datetime import date, datetime
from .interval import Interval, SpikeStatus, ChannelType


class ActualInterval(Interval):
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

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "type": "ActualInterval"
        })
        return d
