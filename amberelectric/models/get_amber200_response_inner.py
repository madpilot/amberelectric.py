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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from amberelectric.models.actual_interval import ActualInterval
from amberelectric.models.current_interval import CurrentInterval
from amberelectric.models.forecast_interval import ForecastInterval
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETAMBER200RESPONSEINNER_ONE_OF_SCHEMAS = ["ActualInterval", "CurrentInterval", "ForecastInterval"]

class GetAmber200ResponseInner(BaseModel):
    """
    GetAmber200ResponseInner
    """
    # data type: ActualInterval
    oneof_schema_1_validator: Optional[ActualInterval] = None
    # data type: CurrentInterval
    oneof_schema_2_validator: Optional[CurrentInterval] = None
    # data type: ForecastInterval
    oneof_schema_3_validator: Optional[ForecastInterval] = None
    actual_instance: Optional[Union[ActualInterval, CurrentInterval, ForecastInterval]] = None
    one_of_schemas: Set[str] = { "ActualInterval", "CurrentInterval", "ForecastInterval" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetAmber200ResponseInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: ActualInterval
        if not isinstance(v, ActualInterval):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActualInterval`")
        else:
            match += 1
        # validate data type: CurrentInterval
        if not isinstance(v, CurrentInterval):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CurrentInterval`")
        else:
            match += 1
        # validate data type: ForecastInterval
        if not isinstance(v, ForecastInterval):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ForecastInterval`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetAmber200ResponseInner with oneOf schemas: ActualInterval, CurrentInterval, ForecastInterval. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetAmber200ResponseInner with oneOf schemas: ActualInterval, CurrentInterval, ForecastInterval. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ActualInterval
        try:
            instance.actual_instance = ActualInterval.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CurrentInterval
        try:
            instance.actual_instance = CurrentInterval.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ForecastInterval
        try:
            instance.actual_instance = ForecastInterval.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetAmber200ResponseInner with oneOf schemas: ActualInterval, CurrentInterval, ForecastInterval. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetAmber200ResponseInner with oneOf schemas: ActualInterval, CurrentInterval, ForecastInterval. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ActualInterval, CurrentInterval, ForecastInterval]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


