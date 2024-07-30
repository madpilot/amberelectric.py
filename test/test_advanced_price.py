# coding: utf-8

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 2.0.0
    Contact: dev@amber.com.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from amberelectric.models.advanced_price import AdvancedPrice  # noqa: E501

class TestAdvancedPrice(unittest.TestCase):
    """AdvancedPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedPrice:
        """Test AdvancedPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedPrice`
        """
        model = AdvancedPrice()  # noqa: E501
        if include_optional:
            return AdvancedPrice(
                low = 1.337,
                high = 1.337
            )
        else:
            return AdvancedPrice(
                low = 1.337,
                high = 1.337,
        )
        """

    def testAdvancedPrice(self):
        """Test AdvancedPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
