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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amberelectric.models.channel_type import ChannelType
from amberelectric.models.price_descriptor import PriceDescriptor
from amberelectric.models.spike_status import SpikeStatus
from amberelectric.models.tariff_information import TariffInformation
from typing import Optional, Set
from typing_extensions import Self

class Usage(BaseModel):
    """
    Usage
    """ # noqa: E501
    type: StrictStr
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
    channel_identifier: StrictStr = Field(description="Meter channel identifier", alias="channelIdentifier")
    kwh: float = Field(description="Number of kWh you consumed or generated. Generated numbers will be negative")
    quality: StrictStr = Field(description="If the metering company has had trouble contacting your meter, they may make an estimate of your usage for that period. Billable data is data that will appear on your bill.")
    cost: float = Field(description="The total cost of your consumption or generation for this period - includes GST")
    __properties: ClassVar[List[str]] = ["type", "duration", "spotPerKwh", "perKwh", "date", "nemTime", "startTime", "endTime", "renewables", "channelType", "tariffInformation", "spikeStatus", "descriptor", "channelIdentifier", "kwh", "quality", "cost"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Usage']):
            raise ValueError("must be one of enum values ('Usage')")
        return value

    @field_validator('duration')
    def duration_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([5, 15, 30]):
            raise ValueError("must be one of enum values (5, 15, 30)")
        return value

    @field_validator('quality')
    def quality_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['estimated', 'billable']):
            raise ValueError("must be one of enum values ('estimated', 'billable')")
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
        """Create an instance of Usage from a JSON string"""
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
        # set to None if tariff_information (nullable) is None
        # and model_fields_set contains the field
        if self.tariff_information is None and "tariff_information" in self.model_fields_set:
            _dict['tariffInformation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Usage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
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
            "channelIdentifier": obj.get("channelIdentifier"),
            "kwh": obj.get("kwh"),
            "quality": obj.get("quality"),
            "cost": obj.get("cost")
        })
        return _obj


