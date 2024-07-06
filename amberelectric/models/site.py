# coding: utf-8

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 1.0
    Contact: dev@amber.com.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amberelectric.models.channel import Channel
from typing import Optional, Set
from typing_extensions import Self

class Site(BaseModel):
    """
    Site
    """ # noqa: E501
    id: StrictStr = Field(description="Unique Site Identifier")
    nmi: Annotated[str, Field(min_length=10, strict=True, max_length=11)] = Field(description="National Metering Identifier (NMI) for the site")
    channels: List[Channel] = Field(description="List of channels that are readable from your meter")
    network: StrictStr = Field(description="The name of the site's network")
    status: StrictStr = Field(description="Site status.  Pending sites are still in the process of being transferred. Note: We only include sites that have correct address details. If you expect to see a site, but don't, you may need to contact [info@amber.com.au](mailto:info@amber.com.au) to check that the address is correct.  Active sites are ones that we actively supply electricity to.  Closed sites are old sites that we no longer supply.")
    active_from: Optional[StrictStr] = Field(default=None, description="Date the site became active. This date will be in the future for pending sites. It may also be undefined, though if it is, contact [info@amber.com.au](mailto:info@amber.com.au) - there may be an issue with your address. Formatted as a ISO 8601 date when present.", alias="activeFrom")
    closed_on: Optional[StrictStr] = Field(default=None, description="Date the site closed. Undefined if the site is pending or active. Formatted as a ISO 8601 date when present.", alias="closedOn")
    __properties: ClassVar[List[str]] = ["id", "nmi", "channels", "network", "status", "activeFrom", "closedOn"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'active', 'closed']):
            raise ValueError("must be one of enum values ('pending', 'active', 'closed')")
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
        """Create an instance of Site from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in channels (list)
        _items = []
        if self.channels:
            for _item in self.channels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['channels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Site from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "nmi": obj.get("nmi"),
            "channels": [Channel.from_dict(_item) for _item in obj["channels"]] if obj.get("channels") is not None else None,
            "network": obj.get("network"),
            "status": obj.get("status"),
            "activeFrom": obj.get("activeFrom"),
            "closedOn": obj.get("closedOn")
        })
        return _obj


