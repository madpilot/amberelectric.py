from typing import Union
from enum import Enum


class PeriodType(Enum):
    OFF_PEAK = "offPeak"
    SHOULDER = "shoulder"
    SOLAR_SPONGE = "solarSponge"
    PEAK = "peak"

    def from_str(s: Union[str, None]):
        possible = list(filter(lambda t: t.value == s, PeriodType))
        if len(possible) > 0:
            return possible[0]


class SeasonType(Enum):
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"
    SPRING = "spring"
    NON_SUMMER = "nonSummer"
    HOLIDAY = "holiday"
    WEEKEND = "weekend"
    WEEKEND_HOLIDAY = "weekendHoliday"
    WEEKDAY = "weekday"

    def from_str(s: Union[str, None]):
        possible = list(filter(lambda t: t.value == s, SeasonType))
        if len(possible) > 0:
            return possible[0]


class TariffInformation(object):
    """Information about how your tariff affects an interval"""

    """The Time of Use period that is currently active. Only available if the site in on a time of use tariff"""
    period: Union[PeriodType, None]

    """The Time of Use season that is currently active. Only available if the site in on a time of use tariff"""
    season: Union[SeasonType, None]

    """The block that is currently active. Only available in the site in on a block tariff"""
    block: Union[int, None]

    """Is this interval currently in the demand window? Only available if the site in on a demand tariff"""
    demand_window: Union[bool, None]

    def __init__(self, **kwargs):
        self.period = PeriodType.from_str(kwargs.get('period'))
        self.season = SeasonType.from_str(kwargs.get('season'))
        self.block = kwargs.get('block')
        self.demand_window = kwargs.get('demandWindow')

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str({'period': self.period, 'season': self.season, 'block': self.block, 'demand_window': self.demand_window})
