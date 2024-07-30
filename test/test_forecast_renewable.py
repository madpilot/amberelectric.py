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

from amberelectric.models.forecast_renewable import ForecastRenewable  # noqa: E501

class TestForecastRenewable(unittest.TestCase):
    """ForecastRenewable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ForecastRenewable:
        """Test ForecastRenewable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ForecastRenewable`
        """
        model = ForecastRenewable()  # noqa: E501
        if include_optional:
            return ForecastRenewable(
                type = 'ForecastRenewable',
                duration = 5,
                var_date = 'Wed May 05 10:00:00 AEST 2021',
                nem_time = '2021-05-06T12:30+10:00',
                start_time = '2021-05-05T02:00:01Z',
                end_time = '2021-05-05T02:30Z',
                renewables = 45,
                descriptor = 'best'
            )
        else:
            return ForecastRenewable(
                type = 'ForecastRenewable',
                duration = 5,
                var_date = 'Wed May 05 10:00:00 AEST 2021',
                nem_time = '2021-05-06T12:30+10:00',
                start_time = '2021-05-05T02:00:01Z',
                end_time = '2021-05-05T02:30Z',
                renewables = 45,
                descriptor = 'best',
        )
        """

    def testForecastRenewable(self):
        """Test ForecastRenewable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
