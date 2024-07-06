# coding: utf-8

"""
    Amber Electric Public API

    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber's wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.

    The version of the OpenAPI document: 2.0.0
    Contact: dev@amber.com.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "amberelectric"
VERSION = "2.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "aiohttp >= 3.0.0",
    "aiohttp-retry >= 2.8.3",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Amber Electric Public API",
    author="Amber Electric Development Team",
    author_email="dev@amber.com.au",
    url="https://github.com/madpilot/amberelectric.py",
    keywords=["OpenAPI", "OpenAPI-Generator", "Amber Electric Public API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache Software License",
    long_description_content_type='text/markdown',
    long_description="""\
    Amber is an Australian-based electricity retailer that pass through the real-time wholesale price of energy.  Because of Amber&#39;s wholesale power prices, you can save hundreds of dollars a year by automating high power devices like air-conditioners, heat pumps and pool pumps.  This Python library provides an interface to the API, allowing you to react to current and forecast prices, as well as download your historic usage.
    """,  # noqa: E501
    package_data={"amberelectric": ["py.typed"]},
)
