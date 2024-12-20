# coding: utf-8

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 2.0.0
    Contact: dev@amber.com.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
from aenum import Enum  # type: ignore
from typing import Type, TypeVar

T = TypeVar("T", bound="SpikeStatus")


try:
    pass

except ImportError:
    pass


class SpikeStatus(str, Enum):
    """
    Indicates whether this interval will potentially spike, or is currently in a spike state
    """

    """
    allowed enum values
    """
    NONE = "none"
    POTENTIAL = "potential"
    SPIKE = "spike"

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T:
        """Create an instance of SpikeStatus from a JSON string"""
        return SpikeStatus(json.loads(json_str))
