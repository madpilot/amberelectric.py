# coding: utf-8

"""
    Amber Electric Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amberelectric.models.advanced_price import AdvancedPrice
from amberelectric.models.channel_type import ChannelType
from amberelectric.models.price_descriptor import PriceDescriptor
from amberelectric.models.range import Range
from amberelectric.models.spike_status import SpikeStatus
from amberelectric.models.tariff_information import TariffInformation
from typing import Optional, Set
from typing_extensions import Self

class CurrentInterval(BaseModel):
    """
    CurrentInterval
    """ # noqa: E501
    duration: StrictInt = Field(description="Length of the interval in minutes.")
    spot_per_kwh: float = Field(description="NEM spot price (c/kWh). This is the price generators get paid to generate electricity, and what drives the variable component of your perKwh price - includes GST", alias="spotPerKwh")
    per_kwh: float = Field(description="Number of cents you will pay per kilowatt-hour (c/kWh) - includes GST", alias="perKwh")
    var_date: date = Field(description="Date the interval belongs to (in NEM time). This may be different to the date component of nemTime, as the last interval of the day ends at 12:00 the following day. Formatted as a ISO 8601 date", alias="date")
    nem_time: datetime = Field(description="The interval's NEM time. This represents the time at the end of the interval UTC+10. Formatted as a ISO 8601 time", alias="nemTime")
    start_time: datetime = Field(description="Start time of the interval in UTC. Formatted as a ISO 8601 time", alias="startTime")
    end_time: datetime = Field(description="End time of the interval in UTC. Formatted as a ISO 8601 time", alias="endTime")
    renewables: Annotated[float, Field(le=100, ge=0)] = Field(description="Percentage of renewables in the grid")
    channel_type: ChannelType = Field(alias="channelType")
    tariff_information: Optional[TariffInformation] = Field(default=None, alias="tariffInformation")
    spike_status: SpikeStatus = Field(alias="spikeStatus")
    descriptor: PriceDescriptor
    type: StrictStr
    range: Optional[Range] = None
    estimate: StrictBool = Field(description="Shows true the current price is an estimate. Shows false is the price has been locked in.")
    advanced_price: Optional[AdvancedPrice] = Field(default=None, description="Amber has created an advanced forecast system, that represents our confidence in the AEMO forecast. The range indicates where we think the price will land for a given interval. The advanced price will only be returned if the current price is an estimate.", alias="advancedPrice")
    __properties: ClassVar[List[str]] = ["duration", "spotPerKwh", "perKwh", "date", "nemTime", "startTime", "endTime", "renewables", "channelType", "tariffInformation", "spikeStatus", "descriptor", "type", "range", "estimate", "advancedPrice"]

    @field_validator('duration')
    def duration_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([5, 15, 30]):
            raise ValueError("must be one of enum values (5, 15, 30)")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CurrentInterval']):
            raise ValueError("must be one of enum values ('CurrentInterval')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CurrentInterval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
        # and model_fields_set contains the field
        if self.tariff_information is None and "tariff_information" in self.model_fields_set:
            _dict['tariffInformation'] = None

        # set to None if range (nullable) is None
        # and model_fields_set contains the field
        if self.range is None and "range" in self.model_fields_set:
            _dict['range'] = None

        # set to None if advanced_price (nullable) is None
        # and model_fields_set contains the field
        if self.advanced_price is None and "advanced_price" in self.model_fields_set:
            _dict['advancedPrice'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CurrentInterval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "duration": obj.get("duration"),
            "spotPerKwh": obj.get("spotPerKwh"),
            "perKwh": obj.get("perKwh"),
            "date": obj.get("date"),
            "nemTime": obj.get("nemTime"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "renewables": obj.get("renewables"),
            "channelType": obj.get("channelType"),
            "tariffInformation": TariffInformation.from_dict(obj["tariffInformation"]) if obj.get("tariffInformation") is not None else None,
            "spikeStatus": obj.get("spikeStatus"),
            "descriptor": obj.get("descriptor"),
            "type": obj.get("type"),
            "range": Range.from_dict(obj["range"]) if obj.get("range") is not None else None,
            "estimate": obj.get("estimate"),
            "advancedPrice": AdvancedPrice.from_dict(obj["advancedPrice"]) if obj.get("advancedPrice") is not None else None
        })
        return _obj


