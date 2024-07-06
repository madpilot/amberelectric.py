# coding: utf-8

"""
    Amber Electric Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amberelectric.models.forecast_renewable import ForecastRenewable

class TestForecastRenewable(unittest.TestCase):
    """ForecastRenewable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ForecastRenewable:
        """Test ForecastRenewable
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ForecastRenewable`
        """
        model = ForecastRenewable()
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
