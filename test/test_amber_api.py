from amberelectric.model.interval import SpikeStatus
from amberelectric.configuration import Configuration
from amberelectric.api.amber_api import AmberApi
from amberelectric.rest import RESTClientObject, RESTResponse
from amberelectric.model.actual_interval import ActualInterval
from amberelectric.model.current_interval import CurrentInterval
from amberelectric.model.forecast_interval import ForecastInterval
from amberelectric.model.usage import Usage
from amberelectric.model.tariff_information import PeriodType, SeasonType
from amberelectric.model.channel import ChannelType
import pytest
from datetime import date, datetime
from dateutil.tz import tzoffset, tzutc


class MockRestResponse(RESTResponse):
    def __init__(self, status, reason, data):
        self.status = status
        self.reason = reason
        self.data = data

    def getheaders(self):
        {}

    def getheader(self, name, default=None):
        return None


@pytest.fixture
def configuration():
    return Configuration(
        access_token='psk_secret_key'
    )


def test_sites_success(mocker, configuration):
    json = """
      [
        {
          "id": "01F5A5CRKMZ5BCX9P1S4V990AM",
          "nmi": "3052282872",
          "channels": [
            {
              "identifier": "E1",
              "type": "general"
            },
            {
              "identifier": "E2",
              "type": "controlledLoad"
            },
            {
              "identifier": "B1",
              "type": "feedIn"
            }
          ]
        }
      ]
    """

    def mock_sites(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites")
        assert(query_params is None)
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", json.encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_sites)

    api = AmberApi(RESTClientObject(configuration))
    sites = api.get_sites()
    assert len(sites) == 1
    site = sites[0]
    assert site.id == "01F5A5CRKMZ5BCX9P1S4V990AM"
    assert site.nmi == "3052282872"
    assert len(site.channels) == 3

    general = site.channels[0]
    assert general.identifier == "E1"
    assert general.type == ChannelType.GENERAL

    controlled_load = site.channels[1]
    assert controlled_load.identifier == "E2"
    assert controlled_load.type == ChannelType.CONTROLLED_LOAD

    feed_in = site.channels[2]
    assert feed_in.identifier == "B1"
    assert feed_in.type == ChannelType.FEED_IN


def test_prices_success(mocker, configuration):
    json = """
      [
        {
          "type": "ActualInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:30:00+10:00",
          "startTime": "2021-05-05T02:00:01Z",
          "endTime": "2021-05-05T02:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "offPeak",
            "season": "summer",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "none"
        },
        {
          "type": "ForecastInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:30:00+10:00",
          "startTime": "2021-05-05T02:00:01Z",
          "endTime": "2021-05-05T02:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "shoulder",
            "season": "winter",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "potential",
          "range": {
            "min": 10,
            "max": 90
          }
        },
        {
          "type": "CurrentInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:30:00+10:00",
          "startTime": "2021-05-05T02:00:01Z",
          "endTime": "2021-05-05T02:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "peak",
            "season": "weekend",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "spike",
          "range": {
            "min": 0,
            "max": 100
          },
          "estimate": true
        }
      ]
    """

    def mock_prices(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites/01F5A5CRKMZ5BCX9P1S4V990AM/prices")
        assert(query_params is None)
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", json.encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_prices)

    api = AmberApi(RESTClientObject(configuration))
    prices = api.get_prices('01F5A5CRKMZ5BCX9P1S4V990AM')
    assert len(prices) == 3

    actual = prices[0]
    current = prices[2]
    forecast = prices[1]

    assert(actual.__class__ == ActualInterval)
    assert(actual.duration == 5)
    assert(actual.spot_per_kwh == 6.12)
    assert(actual.per_kwh == 24.33)
    assert(actual.date == date(2021, 5, 5))
    assert(actual.nem_time == datetime(2021, 5, 6, 12, 30, tzinfo=tzoffset(None, 36000)))
    assert(actual.start_time == datetime(2021, 5, 5, 2, 0, 1, tzinfo=tzutc()))
    assert(actual.end_time == datetime(2021, 5, 5, 2, 30, tzinfo=tzutc()))
    assert(actual.renewables == 45.0)
    assert(actual.channel_type == ChannelType.GENERAL)
    assert(actual.spike_status == SpikeStatus.NO_SPIKE)
    assert(actual.tariff_information.period == PeriodType.OFF_PEAK)
    assert(actual.tariff_information.season == SeasonType.SUMMER)
    assert(actual.tariff_information.block == 2)
    assert(actual.tariff_information.demand_window == True)

    assert(current.__class__ == CurrentInterval)
    assert(current.duration == 5)
    assert(current.spot_per_kwh == 6.12)
    assert(current.per_kwh == 24.33)
    assert(current.date == date(2021, 5, 5))
    assert(current.nem_time == datetime(2021, 5, 6, 12, 30, tzinfo=tzoffset(None, 36000)))
    assert(current.start_time == datetime(2021, 5, 5, 2, 0, 1, tzinfo=tzutc()))
    assert(current.end_time == datetime(2021, 5, 5, 2, 30, tzinfo=tzutc()))
    assert(current.renewables == 45.0)
    assert(current.channel_type == ChannelType.GENERAL)
    assert(current.spike_status == SpikeStatus.SPIKE)
    assert(current.tariff_information.period == PeriodType.PEAK)
    assert(current.tariff_information.season == SeasonType.WEEKEND)
    assert(current.tariff_information.block == 2)
    assert(current.tariff_information.demand_window == True)
    assert(current.range.min == 0)
    assert(current.range.max == 100)
    assert(current.estimate == True)

    assert(forecast.__class__ == ForecastInterval)
    assert(forecast.duration == 5)
    assert(forecast.spot_per_kwh == 6.12)
    assert(forecast.per_kwh == 24.33)
    assert(forecast.date == date(2021, 5, 5))
    assert(forecast.nem_time == datetime(2021, 5, 6, 12, 30, tzinfo=tzoffset(None, 36000)))
    assert(forecast.start_time == datetime(2021, 5, 5, 2, 0, 1, tzinfo=tzutc()))
    assert(forecast.end_time == datetime(2021, 5, 5, 2, 30, tzinfo=tzutc()))
    assert(forecast.renewables == 45.0)
    assert(forecast.channel_type == ChannelType.GENERAL)
    assert(forecast.spike_status == SpikeStatus.POTENTIAL)
    assert(forecast.tariff_information.period == PeriodType.SHOULDER)
    assert(forecast.tariff_information.season == SeasonType.WINTER)
    assert(forecast.tariff_information.block == 2)
    assert(forecast.tariff_information.demand_window == True)
    assert(forecast.range.min == 10)
    assert(forecast.range.max == 90)


def test_prices_params(mocker, configuration):
    def mock_prices(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites/01F5A5CRKMZ5BCX9P1S4V990AM/prices")
        assert(query_params == {'startDate': '2021-05-05',
                                'endDate': '2021-05-06', 'resolution': '30'})
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", "[]".encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_prices)

    api = AmberApi(RESTClientObject(configuration))
    api.get_prices('01F5A5CRKMZ5BCX9P1S4V990AM', start_date=date(
        2021, 5, 5), end_date=date(2021, 5, 6), resolution=30)


def test_current_price_success(mocker, configuration):
    json = """
      [
        {
          "type": "CurrentInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:30:00+10:00",
          "startTime": "2021-05-05T02:00:01Z",
          "endTime": "2021-05-05T02:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "offPeak",
            "season": "summer",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "none",
          "range": {
            "min": 0,
            "max": 0
          },
          "estimate": true
        }
      ]
    """

    def mock_prices(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites/01F5A5CRKMZ5BCX9P1S4V990AM/prices/current")
        assert(query_params is None)
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", json.encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_prices)

    api = AmberApi(RESTClientObject(configuration))
    prices = api.get_current_price('01F5A5CRKMZ5BCX9P1S4V990AM')
    assert len(prices) == 1

    current = prices[0]

    assert(current.__class__ == CurrentInterval)
    assert(current.duration == 5)
    assert(current.spot_per_kwh == 6.12)
    assert(current.per_kwh == 24.33)
    assert(current.date == date(2021, 5, 5))
    assert(current.nem_time == datetime(2021, 5, 6, 12, 30, tzinfo=tzoffset(None, 36000)))
    assert(current.start_time == datetime(2021, 5, 5, 2, 0, 1, tzinfo=tzutc()))
    assert(current.end_time == datetime(2021, 5, 5, 2, 30, tzinfo=tzutc()))
    assert(current.renewables == 45.0)
    assert(current.channel_type == ChannelType.GENERAL)
    assert(current.spike_status == SpikeStatus.NO_SPIKE)
    assert(current.tariff_information.period == PeriodType.OFF_PEAK)
    assert(current.tariff_information.season == SeasonType.SUMMER)
    assert(current.tariff_information.block == 2)
    assert(current.tariff_information.demand_window == True)
    assert(current.range.min == 0)
    assert(current.range.max == 0)
    assert(current.estimate == True)


def test_current_prices_params(mocker, configuration):
    json = """
      [
        {
          "type": "ActualInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:00:00+10:00",
          "startTime": "2021-05-05T01:30:01Z",
          "endTime": "2021-05-05T02:00:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "offPeak",
            "season": "summer",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "none"
        },
        {
          "type": "CurrentInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:30:00+10:00",
          "startTime": "2021-05-05T02:00:01Z",
          "endTime": "2021-05-05T02:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "peak",
            "season": "weekend",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "spike",
          "range": {
            "min": 0,
            "max": 100
          },
          "estimate": true
        },
        {
          "type": "ForecastInterval",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T01:30:00+10:00",
          "startTime": "2021-05-05T03:00:01Z",
          "endTime": "2021-05-05T03:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "shoulder",
            "season": "winter",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "potential",
          "range": {
            "min": 10,
            "max": 90
          }
        }
      ]
    """

    def mock_prices(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites/01F5A5CRKMZ5BCX9P1S4V990AM/prices/current")
        assert(query_params == {'resolution': '30', 'next': '1', 'previous': '1'})
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", json.encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_prices)

    api = AmberApi(RESTClientObject(configuration))
    prices = api.get_current_price('01F5A5CRKMZ5BCX9P1S4V990AM', resolution=30, next=1, previous=1)
    assert len(prices) == 3
    assert(prices[0].__class__ == ActualInterval)
    assert(prices[1].__class__ == CurrentInterval)
    assert(prices[2].__class__ == ForecastInterval)


def test_usage_success(mocker, configuration):
    json = """
      [
        {
          "type": "Usage",
          "duration": 5,
          "spotPerKwh": 6.12,
          "perKwh": 24.33,
          "date": "2021-05-05",
          "nemTime": "2021-05-06T12:30:00+10:00",
          "startTime": "2021-05-05T02:00:01Z",
          "endTime": "2021-05-05T02:30:00Z",
          "renewables": 45,
          "channelType": "general",
          "tariffInformation": {
            "period": "offPeak",
            "season": "summer",
            "block": 2,
            "demandWindow": true
          },
          "spikeStatus": "none",
          "channelIdentifier": "E1",
          "kwh": 1,
          "quality": "estimated",
          "cost": 2
        }
      ]
    """

    def mock_prices(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites/01F5A5CRKMZ5BCX9P1S4V990AM/usage")
        assert(query_params == {'startDate': '2021-05-05', 'endDate': '2021-05-06'})
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", json.encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_prices)

    api = AmberApi(RESTClientObject(configuration))
    prices = api.get_usage('01F5A5CRKMZ5BCX9P1S4V990AM', date(2021, 5, 5), date(2021, 5, 6))
    assert len(prices) == 1

    usage = prices[0]

    assert(usage.__class__ == Usage)
    assert(usage.duration == 5)
    assert(usage.spot_per_kwh == 6.12)
    assert(usage.per_kwh == 24.33)
    assert(usage.date == date(2021, 5, 5))
    assert(usage.nem_time == datetime(2021, 5, 6, 12, 30, tzinfo=tzoffset(None, 36000)))
    assert(usage.start_time == datetime(2021, 5, 5, 2, 0, 1, tzinfo=tzutc()))
    assert(usage.end_time == datetime(2021, 5, 5, 2, 30, tzinfo=tzutc()))
    assert(usage.renewables == 45.0)
    assert(usage.channel_type == ChannelType.GENERAL)
    assert(usage.spike_status == SpikeStatus.NO_SPIKE)
    assert(usage.tariff_information.period == PeriodType.OFF_PEAK)
    assert(usage.tariff_information.season == SeasonType.SUMMER)
    assert(usage.tariff_information.block == 2)
    assert(usage.tariff_information.demand_window == True)
    assert(usage.kwh == 1)
    assert(usage.quality == 'estimated')
    assert(usage.cost == 2)
    assert(usage.channelIdentifier == "E1")


def test_usage_success_params(mocker, configuration):
    def mock_prices(self, method, path, query_params=None, headers=None, body=None, post_params=None, _preload_content=True, _request_timeout=None):
        assert(method == "GET")
        assert(path == "https://api.amber.com.au/v1/sites/01F5A5CRKMZ5BCX9P1S4V990AM/usage")
        assert(query_params == {'startDate': '2021-05-05',
                                'endDate': '2021-05-06', 'resolution': '30'})
        assert(headers == {'Authorization': 'Bearer psk_secret_key'})
        return MockRestResponse(200, "", "[]".encode('utf-8'))

    mocker.patch('amberelectric.rest.RESTClientObject.request', mock_prices)

    api = AmberApi(RESTClientObject(configuration))
    api.get_usage('01F5A5CRKMZ5BCX9P1S4V990AM', date(2021, 5, 5), date(2021, 5, 6), resolution=30)
