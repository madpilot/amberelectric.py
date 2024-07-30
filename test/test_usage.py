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

from amberelectric.models.usage import Usage  # noqa: E501

class TestUsage(unittest.TestCase):
    """Usage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Usage:
        """Test Usage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Usage`
        """
        model = Usage()  # noqa: E501
        if include_optional:
            return Usage(
                type = 'Usage',
                duration = 5,
                spot_per_kwh = 6.12,
                per_kwh = 24.33,
                var_date = 'Wed May 05 10:00:00 AEST 2021',
                nem_time = '2021-05-06T12:30+10:00',
                start_time = '2021-05-05T02:00:01Z',
                end_time = '2021-05-05T02:30Z',
                renewables = 45,
                channel_type = 'general',
                tariff_information = amberelectric.models.tariff_information.TariffInformation(
                    period = 'offPeak', 
                    season = 'default', 
                    block = 1, 
                    demand_window = True, ),
                spike_status = 'none',
                descriptor = 'negative',
                channel_identifier = 'E1',
                kwh = 1.337,
                quality = 'estimated',
                cost = 1.337
            )
        else:
            return Usage(
                type = 'Usage',
                duration = 5,
                spot_per_kwh = 6.12,
                per_kwh = 24.33,
                var_date = 'Wed May 05 10:00:00 AEST 2021',
                nem_time = '2021-05-06T12:30+10:00',
                start_time = '2021-05-05T02:00:01Z',
                end_time = '2021-05-05T02:30Z',
                renewables = 45,
                channel_type = 'general',
                spike_status = 'none',
                descriptor = 'negative',
                channel_identifier = 'E1',
                kwh = 1.337,
                quality = 'estimated',
                cost = 1.337,
        )
        """

    def testUsage(self):
        """Test Usage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
