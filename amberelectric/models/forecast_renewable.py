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

from pydantic import BaseModel, Field, StrictInt, StrictStr, confloat, validator
from amberelectric.models.renewable_descriptor import RenewableDescriptor

class ForecastRenewable(BaseModel):
    """
    ForecastRenewable
    """
    type: StrictStr = Field(...)
    duration: StrictInt = Field(default=..., description="Length of the interval in minutes.")
    var_date: date = Field(default=..., alias="date", description="Date the interval belongs to (in NEM time). This may be different to the date component of nemTime, as the last interval of the day ends at 12:00 the following day. Formatted as a ISO 8601 date")
    nem_time: datetime = Field(default=..., alias="nemTime", description="The interval's NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time")
    start_time: datetime = Field(default=..., alias="startTime", description="Start time of the interval in UTC. Formatted as a ISO 8601 time")
    end_time: datetime = Field(default=..., alias="endTime", description="End time of the interval in UTC. Formatted as a ISO 8601 time")
    renewables: confloat(le=100, ge=0) = Field(default=..., description="Percentage of renewables in the grid")
    descriptor: RenewableDescriptor = Field(...)
    __properties = ["type", "duration", "date", "nemTime", "startTime", "endTime", "renewables", "descriptor"]

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
    def from_json(cls, json_str: str) -> ForecastRenewable:
        """Create an instance of ForecastRenewable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ForecastRenewable:
        """Create an instance of ForecastRenewable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ForecastRenewable.parse_obj(obj)

        _obj = ForecastRenewable.parse_obj({
            "type": obj.get("type"),
            "duration": obj.get("duration"),
            "var_date": obj.get("date"),
            "nem_time": obj.get("nemTime"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "renewables": obj.get("renewables"),
            "descriptor": obj.get("descriptor")
        })
        return _obj


