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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TariffInformation(BaseModel):
    """
    Information about how your tariff affects an interval
    """ # noqa: E501
    period: Optional[StrictStr] = Field(default=None, description="The Time of Use period that is currently active. Only available if the site in on a time of use tariff")
    season: Optional[StrictStr] = Field(default=None, description="The Time of Use season that is currently active. Only available if the site in on a time of use tariff")
    block: Optional[Annotated[float, Field(le=2, ge=1)]] = Field(default=None, description="The block that is currently active. Only available in the site in on a block tariff")
    demand_window: Optional[StrictBool] = Field(default=None, description="Is this interval currently in the demand window? Only available if the site in on a demand tariff", alias="demandWindow")
    __properties: ClassVar[List[str]] = ["period", "season", "block", "demandWindow"]

    @field_validator('period')
    def period_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['offPeak', 'shoulder', 'solarSponge', 'peak']):
            raise ValueError("must be one of enum values ('offPeak', 'shoulder', 'solarSponge', 'peak')")
        return value

    @field_validator('season')
    def season_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'summer', 'autumn', 'winter', 'spring', 'nonSummer', 'holiday', 'weekend', 'weekendHoliday', 'weekday']):
            raise ValueError("must be one of enum values ('default', 'summer', 'autumn', 'winter', 'spring', 'nonSummer', 'holiday', 'weekend', 'weekendHoliday', 'weekday')")
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
        """Create an instance of TariffInformation from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TariffInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "period": obj.get("period"),
            "season": obj.get("season"),
            "block": obj.get("block"),
            "demandWindow": obj.get("demandWindow")
        })
        return _obj


