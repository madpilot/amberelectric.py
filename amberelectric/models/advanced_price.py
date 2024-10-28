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


try:

    from pydantic.v1 import BaseModel, Field
except ImportError:

    from pydantic import BaseModel, Field


class AdvancedPrice(BaseModel):
    """
    Amber has created an advanced forecast system, that represents our confidence in the AEMO forecast. The range indicates where we think the price will land for a given interval.  # noqa: E501
    """

    low: float = Field(
        default=...,
        description="The lower bound of our prediction band. Price includes network and market fees. (c/kWh).",
    )
    predicted: float = Field(
        default=...,
        description="The predicted price. Use this if you need a single number for forecasting against. Price includes network and market fees. (c/kWh).",
    )
    high: float = Field(
        default=...,
        description="The upper bound of our prediction band. Price includes network and market fees. (c/kWh).",
    )
    __properties = ["low", "predicted", "high"]

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
    def from_json(cls, json_str: str) -> AdvancedPrice:
        """Create an instance of AdvancedPrice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedPrice:
        """Create an instance of AdvancedPrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedPrice.parse_obj(obj)

        _obj = AdvancedPrice.parse_obj(
            {
                "low": obj.get("low"),
                "predicted": obj.get("predicted"),
                "high": obj.get("high"),
            }
        )
        return _obj
