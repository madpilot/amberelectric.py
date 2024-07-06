# coding: utf-8

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amberelectric.api.sites_api import SitesApi


class TestSitesApi(unittest.TestCase):
    """SitesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SitesApi()

    def tearDown(self) -> None:
        pass

    def test_get_current_prices(self) -> None:
        """Test case for get_current_prices

        """
        pass

    def test_get_prices(self) -> None:
        """Test case for get_prices

        """
        pass

    def test_get_sites(self) -> None:
        """Test case for get_sites

        """
        pass

    def test_get_usage(self) -> None:
        """Test case for get_usage

        """
        pass


if __name__ == '__main__':
    unittest.main()
