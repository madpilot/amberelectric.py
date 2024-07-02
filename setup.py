from setuptools import setup, find_packages  # noqa: H301

NAME = "amberelectric"
VERSION = "1.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author="Amber Electric",
    author_email="dev+pypi@amber.com.au",
    url="https://github.com/madpilot/amberelectric.py",
    keywords=["amberelectric"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    description="Interface to the Amber Electric API, allowing you to download current and forecast price, as well as download your historic usage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers = [
      "License :: OSI Approved :: Apache Software License",
    ]
)
