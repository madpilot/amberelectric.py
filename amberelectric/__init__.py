# coding: utf-8

# flake8: noqa

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 2.0.0
    Contact: dev@amber.com.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "2.0.12"

# import apis into sdk package
from amberelectric.api.amber_api import AmberApi

# import ApiClient
from amberelectric.api_response import ApiResponse
from amberelectric.api_client import ApiClient
from amberelectric.configuration import Configuration
from amberelectric.exceptions import OpenApiException
from amberelectric.exceptions import ApiTypeError
from amberelectric.exceptions import ApiValueError
from amberelectric.exceptions import ApiKeyError
from amberelectric.exceptions import ApiAttributeError
from amberelectric.exceptions import ApiException

# import models into sdk package
from amberelectric.models.actual_interval import ActualInterval
from amberelectric.models.actual_renewable import ActualRenewable
from amberelectric.models.advanced_price import AdvancedPrice
from amberelectric.models.base_interval import BaseInterval
from amberelectric.models.base_renewable import BaseRenewable
from amberelectric.models.channel import Channel
from amberelectric.models.channel_type import ChannelType
from amberelectric.models.current_interval import CurrentInterval
from amberelectric.models.current_renewable import CurrentRenewable
from amberelectric.models.forecast_interval import ForecastInterval
from amberelectric.models.forecast_renewable import ForecastRenewable
from amberelectric.models.interval import Interval
from amberelectric.models.price_descriptor import PriceDescriptor
from amberelectric.models.range import Range
from amberelectric.models.renewable import Renewable
from amberelectric.models.renewable_descriptor import RenewableDescriptor
from amberelectric.models.site import Site
from amberelectric.models.site_status import SiteStatus
from amberelectric.models.spike_status import SpikeStatus
from amberelectric.models.tariff_information import TariffInformation
from amberelectric.models.usage import Usage
