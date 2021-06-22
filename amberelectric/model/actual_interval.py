from .interval import Interval


class ActualInterval(Interval):
    def __init__(
        self,
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
