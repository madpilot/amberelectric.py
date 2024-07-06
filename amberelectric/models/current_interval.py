# coding: utf-8

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 2.0.0
    Contact: dev@amber.com.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, confloat, validator
from amberelectric.models.advanced_price import AdvancedPrice
from amberelectric.models.channel_type import ChannelType
from amberelectric.models.price_descriptor import PriceDescriptor
from amberelectric.models.range import Range
from amberelectric.models.spike_status import SpikeStatus
from amberelectric.models.tariff_information import TariffInformation

class CurrentInterval(BaseModel):
    """
    CurrentInterval
    """
    type: StrictStr = Field(...)
    duration: StrictInt = Field(default=..., description="Length of the interval in minutes.")
    spot_per_kwh: float = Field(default=..., alias="spotPerKwh", description="NEM spot price (c/kWh). This is the price generators get paid to generate electricity, and what drives the variable component of your perKwh price - includes GST")
    per_kwh: float = Field(default=..., alias="perKwh", description="Number of cents you will pay per kilowatt-hour (c/kWh) - includes GST")
    var_date: date = Field(default=..., alias="date", description="Date the interval belongs to (in NEM time). This may be different to the date component of nemTime, as the last interval of the day ends at 12:00 the following day. Formatted as a ISO 8601 date")
    nem_time: datetime = Field(default=..., alias="nemTime", description="The interval's NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time")
    start_time: datetime = Field(default=..., alias="startTime", description="Start time of the interval in UTC. Formatted as a ISO 8601 time")
    end_time: datetime = Field(default=..., alias="endTime", description="End time of the interval in UTC. Formatted as a ISO 8601 time")
    renewables: confloat(le=100, ge=0) = Field(default=..., description="Percentage of renewables in the grid")
    channel_type: ChannelType = Field(default=..., alias="channelType")
    tariff_information: Optional[TariffInformation] = Field(default=None, alias="tariffInformation")
    spike_status: SpikeStatus = Field(default=..., alias="spikeStatus")
    descriptor: PriceDescriptor = Field(...)
    range: Optional[Range] = None
    estimate: StrictBool = Field(default=..., description="Shows true the current price is an estimate. Shows false is the price has been locked in.")
    advanced_price: Optional[AdvancedPrice] = Field(default=None, alias="advancedPrice", description="Amber has created an advanced forecast system, that represents our confidence in the AEMO forecast. The range indicates where we think the price will land for a given interval. The advanced price will only be returned if the current price is an estimate.")
    __properties = ["type", "duration", "spotPerKwh", "perKwh", "date", "nemTime", "startTime", "endTime", "renewables", "channelType", "tariffInformation", "spikeStatus", "descriptor", "range", "estimate", "advancedPrice"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CurrentInterval'):
            raise ValueError("must be one of enum values ('CurrentInterval')")
        return value

    @validator('duration')
    def duration_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (5, 15, 30):
            raise ValueError("must be one of enum values (5, 15, 30)")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CurrentInterval:
        """Create an instance of CurrentInterval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of tariff_information
        if self.tariff_information:
            _dict['tariffInformation'] = self.tariff_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict['range'] = self.range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of advanced_price
        if self.advanced_price:
            _dict['advancedPrice'] = self.advanced_price.to_dict()
        # set to None if tariff_information (nullable) is None
        # and __fields_set__ contains the field
        if self.tariff_information is None and "tariff_information" in self.__fields_set__:
            _dict['tariffInformation'] = None

        # set to None if range (nullable) is None
        # and __fields_set__ contains the field
        if self.range is None and "range" in self.__fields_set__:
            _dict['range'] = None

        # set to None if advanced_price (nullable) is None
        # and __fields_set__ contains the field
        if self.advanced_price is None and "advanced_price" in self.__fields_set__:
            _dict['advancedPrice'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrentInterval:
        """Create an instance of CurrentInterval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrentInterval.parse_obj(obj)

        _obj = CurrentInterval.parse_obj({
            "type": obj.get("type"),
            "duration": obj.get("duration"),
            "spot_per_kwh": obj.get("spotPerKwh"),
            "per_kwh": obj.get("perKwh"),
            "var_date": obj.get("date"),
            "nem_time": obj.get("nemTime"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "renewables": obj.get("renewables"),
            "channel_type": obj.get("channelType"),
            "tariff_information": TariffInformation.from_dict(obj.get("tariffInformation")) if obj.get("tariffInformation") is not None else None,
            "spike_status": obj.get("spikeStatus"),
            "descriptor": obj.get("descriptor"),
            "range": Range.from_dict(obj.get("range")) if obj.get("range") is not None else None,
            "estimate": obj.get("estimate"),
            "advanced_price": AdvancedPrice.from_dict(obj.get("advancedPrice")) if obj.get("advancedPrice") is not None else None
        })
        return _obj


