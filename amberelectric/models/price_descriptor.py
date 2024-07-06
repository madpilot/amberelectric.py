# coding: utf-8

"""
    Amber Electric Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PriceDescriptor(str, Enum):
    """
    Describes the current price. Gives you an indication of how cheap the price is in relation to the average VMO and DMO. Note: Negative is no longer used. It has been replaced with extremelyLow.
    """

    """
    allowed enum values
    """
    NEGATIVE = 'negative'
    EXTREMELYLOW = 'extremelyLow'
    VERYLOW = 'veryLow'
    LOW = 'low'
    NEUTRAL = 'neutral'
    HIGH = 'high'
    SPIKE = 'spike'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PriceDescriptor from a JSON string"""
        return cls(json.loads(json_str))


