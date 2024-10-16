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
from aenum import Enum # type: ignore


try: 
    pass
    
except ImportError:
    pass
    

class SiteStatus(str, Enum):
    """
    Site status.  Pending sites are still in the process of being transferred. Note: We only include sites that have correct address details. If you expect to see a site, but don't, you may need to contact [info@amber.com.au](mailto:info@amber.com.au) to check that the address is correct.  Active sites are ones that we actively supply electricity to.  Closed sites are old sites that we no longer supply.
    """

    """
    allowed enum values
    """
    PENDING = 'pending'
    ACTIVE = 'active'
    CLOSED = 'closed'

    @classmethod
    def from_json(cls, json_str: str) -> SiteStatus:
        """Create an instance of SiteStatus from a JSON string"""
        return SiteStatus(json.loads(json_str))


