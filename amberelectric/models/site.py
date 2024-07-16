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

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from amberelectric.models.channel import Channel
from amberelectric.models.site_status import SiteStatus

class Site(BaseModel):
    """
    Site
    """
    id: StrictStr = Field(default=..., description="Unique Site Identifier")
    nmi: constr(strict=True, max_length=11, min_length=10) = Field(default=..., description="National Metering Identifier (NMI) for the site")
    channels: conlist(Channel) = Field(default=..., description="List of channels that are readable from your meter")
    network: StrictStr = Field(default=..., description="The name of the site's network")
    status: SiteStatus = Field(...)
    active_from: Optional[date] = Field(default=None, alias="activeFrom", description="Date the site became active. This date will be in the future for pending sites. It may also be undefined, though if it is, contact [info@amber.com.au](mailto:info@amber.com.au) - there may be an issue with your address. Formatted as a ISO 8601 date when present.")
    closed_on: Optional[date] = Field(default=None, alias="closedOn", description="Date the site closed. Undefined if the site is pending or active. Formatted as a ISO 8601 date when present.")
    __properties = ["id", "nmi", "channels", "network", "status", "activeFrom", "closedOn"]

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
    def from_json(cls, json_str: str) -> Site:
        """Create an instance of Site from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in channels (list)
        _items = []
        if self.channels:
            for _item in self.channels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['channels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Site:
        """Create an instance of Site from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Site.parse_obj(obj)

        _obj = Site.parse_obj({
            "id": obj.get("id"),
            "nmi": obj.get("nmi"),
            "channels": [Channel.from_dict(_item) for _item in obj.get("channels")] if obj.get("channels") is not None else None,
            "network": obj.get("network"),
            "status": obj.get("status"),
            "active_from": obj.get("activeFrom"),
            "closed_on": obj.get("closedOn")
        })
        return _obj


