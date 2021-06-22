from typing import List, Optional, Union
import json
import dateutil.parser
from datetime import date

from ..rest import RESTResponse
from ..configuration import Configuration
from ..model.site import Site
from ..model.current_interval import CurrentInterval
from ..model.actual_interval import ActualInterval
from ..model.forecast_interval import ForecastInterval
from ..model.usage import Usage
from ..model.tariff_information import TariffInformation
from ..model.channel import Channel
from ..model.range import Range
from ..exceptions import ApiException

from ..rest import RESTClientObject


def parse_tariff_information(tariff_information: Optional[object]) -> TariffInformation:
    if tariff_information is None:
        return None
    else:
        return TariffInformation(tariff_information)


def parse_range(range: Optional[object]) -> Range:
    if range is None:
        return None
    else:
        return Range(float(range['min']), float(range['max']))


def parse_interval(interval: object) -> Union[ActualInterval, CurrentInterval, ForecastInterval, Usage]:
    optional = {}

    if 'tariff_information' in interval:
        optional['tariff_information'] = parse_tariff_information(interval['tariff_information'])

    if 'range' in interval:
        optional['range'] = parse_range(interval['range'])

    if interval['type'] == 'ActualInterval':
        return ActualInterval(
            float(interval['duration']),
            float(interval['spotPerKwh']),
            float(interval['perKwh']),
            dateutil.parser.isoparse(interval['date']).date(),
            dateutil.parser.isoparse(interval['nemTime']),
            dateutil.parser.isoparse(interval['startTime']),
            dateutil.parser.isoparse(interval['endTime']),
            float(interval['renewables']),
            interval['channelType'],
            interval['spikeStatus'],
            **optional
        )

    if interval['type'] == 'CurrentInterval':
        return CurrentInterval(
            float(interval['duration']),
            float(interval['spotPerKwh']),
            float(interval['perKwh']),
            dateutil.parser.isoparse(interval['date']).date(),
            dateutil.parser.isoparse(interval['nemTime']),
            dateutil.parser.isoparse(interval['startTime']),
            dateutil.parser.isoparse(interval['endTime']),
            float(interval['renewables']),
            interval['channelType'],
            interval['spikeStatus'],
            interval['estimate'],
            **optional
        )

    if interval['type'] == 'ForecastInterval':
        return ForecastInterval(
            float(interval['duration']),
            float(interval['spotPerKwh']),
            float(interval['perKwh']),
            dateutil.parser.isoparse(interval['date']).date(),
            dateutil.parser.isoparse(interval['nemTime']),
            dateutil.parser.isoparse(interval['startTime']),
            dateutil.parser.isoparse(interval['endTime']),
            float(interval['renewables']),
            interval['channelType'],
            interval['spikeStatus'],
            **optional
        )

    if interval['type'] == 'Usage':
        if 'channelIdentifier' in interval:
            optional['channelIdentifier'] = interval['channelIdentifier']

        return Usage(
            float(interval['duration']),
            float(interval['spotPerKwh']),
            float(interval['perKwh']),
            dateutil.parser.isoparse(interval['date']).date(),
            dateutil.parser.isoparse(interval['nemTime']),
            dateutil.parser.isoparse(interval['startTime']),
            dateutil.parser.isoparse(interval['endTime']),
            float(interval['renewables']),
            interval['channelType'],
            interval['spikeStatus'],
            float(interval['kwh']),
            interval['quality'],
            float(interval['cost']),
            **optional
        )


def parse_intervals(intervals: List[object]) -> List[Union[ActualInterval, CurrentInterval, ForecastInterval, Usage]]:
    return list(map(parse_interval, intervals))


def parse_channel(channel: object) -> Channel:
    return Channel(channel['identifier'], channel['type'])


def parse_channels(channels: List[object]) -> List[Channel]:
    return list(map(parse_channel, channels))


def parse_site(site: object) -> Site:
    return Site(site['id'], site['nmi'], parse_channels(site['channels']))


def parse_sites(sites: List[object]) -> List[Site]:
    return list(map(parse_site, sites))


class AmberApi:
    def __init__(self, rest_client: RESTClientObject):
        self._rest_client = rest_client

    def create(configuration: Configuration):
        return AmberApi(RESTClientObject(configuration))

    def request(self, method, path, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None) -> RESTResponse:
        auth = self._rest_client.configuration.auth_settings()
        if 'apiKey' in auth:
            token = auth['apiKey']
            if headers is None:
                headers = {}
            headers[token['key']] = token['value']

        url = self._rest_client.configuration.host + path
        return self._rest_client.request(method, url, query_params, headers, body, post_params, _preload_content, _request_timeout)

    def get_sites(self) -> List[Site]:
        response = self.request("GET", "/sites")
        if response.status == 200:
            return parse_sites(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)

    def get_current_price(self, site_id: str, **kwargs) -> List[CurrentInterval]:
        query_params = {}
        if "resolution" in kwargs:
            query_params["resolution"] = kwargs.get("resolution")

        if query_params == {}:
            query_params = None
        response = self.request("GET", "/sites/" + site_id + "/prices/current", query_params)

        if response.status == 200:
            return parse_intervals(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)

    def get_prices(self, site_id: str, **kwargs) -> Union[ActualInterval, CurrentInterval, ForecastInterval]:
        query_params = {}
        if "end_date" in kwargs:
            query_params["endDate"] = kwargs.get("end_date")
        if "start_date" in kwargs:
            query_params["startDate"] = kwargs.get("start_date")
        if "resolution" in kwargs:
            query_params["resolution"] = kwargs.get("resolution")

        if query_params == {}:
            query_params = None

        response = self.request("GET", "/sites/" + site_id + "/prices", query_params)

        if response.status == 200:
            return parse_intervals(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)

    def get_usage(self, site_id: str, start_date: date, end_date: date, **kwargs) -> Usage:
        query_params = {'startDate': start_date, 'endDate': end_date}
        if "resolution" in kwargs:
            query_params["resolution"] = kwargs.get("resolution")

        response = self.request("GET", "/sites/" + site_id + "/usage", query_params)

        if response.status == 200:
            return parse_intervals(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)
