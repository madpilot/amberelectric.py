from typing import List, Optional, Union
import json
from dateutil import parser
from datetime import date

from amberelectric.rest import RESTResponse
from amberelectric.configuration import Configuration
from amberelectric.model.site import Site, SiteStatus
from amberelectric.model.current_interval import CurrentInterval
from amberelectric.model.actual_interval import ActualInterval
from amberelectric.model.forecast_interval import ForecastInterval
from amberelectric.model.usage import Usage
from amberelectric.model.tariff_information import TariffInformation
from amberelectric.model.channel import Channel, ChannelType
from amberelectric.model.range import Range
from amberelectric.exceptions import ApiException

from ..rest import RESTClientObject

ISO_DATE_FORMAT = "%Y-%m-%d"


def parse_tariff_information(
    tariff_information: Optional[dict],
) -> Union[TariffInformation, None]:
    if tariff_information is None:
        return None
    else:
        return TariffInformation(**tariff_information)


def parse_range(range: Optional[dict]) -> Union[Range, None]:
    if range is None:
        return None
    else:
        return Range(float(range["min"]), float(range["max"]))


def parse_interval(
    interval: dict,
) -> Union[ActualInterval, CurrentInterval, ForecastInterval, Usage]:
    optional = {}

    if "tariffInformation" in interval:
        optional["tariff_information"] = parse_tariff_information(
            interval["tariffInformation"]
        )

    if "range" in interval:
        optional["range"] = parse_range(interval["range"])

    if interval["type"] == "ActualInterval":
        return ActualInterval(
            float(interval["duration"]),
            float(interval["spotPerKwh"]),
            float(interval["perKwh"]),
            parser.isoparse(interval["date"]).date(),
            parser.isoparse(interval["nemTime"]),
            parser.isoparse(interval["startTime"]),
            parser.isoparse(interval["endTime"]),
            float(interval["renewables"]),
            interval["channelType"],
            interval["spikeStatus"],
            interval["descriptor"],
            **optional
        )

    if interval["type"] == "CurrentInterval":
        return CurrentInterval(
            float(interval["duration"]),
            float(interval["spotPerKwh"]),
            float(interval["perKwh"]),
            parser.isoparse(interval["date"]).date(),
            parser.isoparse(interval["nemTime"]),
            parser.isoparse(interval["startTime"]),
            parser.isoparse(interval["endTime"]),
            float(interval["renewables"]),
            interval["channelType"],
            interval["spikeStatus"],
            interval["descriptor"],
            interval["estimate"],
            **optional
        )

    if interval["type"] == "ForecastInterval":
        return ForecastInterval(
            float(interval["duration"]),
            float(interval["spotPerKwh"]),
            float(interval["perKwh"]),
            parser.isoparse(interval["date"]).date(),
            parser.isoparse(interval["nemTime"]),
            parser.isoparse(interval["startTime"]),
            parser.isoparse(interval["endTime"]),
            float(interval["renewables"]),
            interval["channelType"],
            interval["spikeStatus"],
            interval["descriptor"],
            **optional
        )

    if interval["type"] == "Usage":
        return Usage(
            float(interval["duration"]),
            float(interval["spotPerKwh"]),
            float(interval["perKwh"]),
            parser.isoparse(interval["date"]).date(),
            parser.isoparse(interval["nemTime"]),
            parser.isoparse(interval["startTime"]),
            parser.isoparse(interval["endTime"]),
            float(interval["renewables"]),
            interval["channelType"],
            interval["spikeStatus"],
            interval["descriptor"],
            interval["channelIdentifier"],
            float(interval["kwh"]),
            interval["quality"],
            float(interval["cost"]),
            **optional
        )
    raise TypeError("Unknown type")


def parse_intervals(
    intervals: List[dict],
) -> List[Union[ActualInterval, CurrentInterval, ForecastInterval, Usage]]:
    return [parse_interval(interval) for interval in intervals]


def parse_channel(channel: dict) -> Channel:
    return Channel(
        channel["identifier"], ChannelType.from_str(channel["type"]), channel["tariff"]
    )


def parse_channels(channels: List[dict]) -> List[Channel]:
    return [parse_channel(channel) for channel in channels]


def parse_site(site: dict) -> Site:
    active_from = (
        parser.isoparse(site["activeFrom"]).date() if "activeFrom" in site else None
    )

    closed_on = parser.isoparse(site["closedOn"]).date() if "closedOn" in site else None

    return Site(
        site["id"],
        site["nmi"],
        parse_channels(site["channels"]),
        site["network"],
        SiteStatus.from_str(site["status"]),
        active_from,
        closed_on,
    )


def parse_sites(sites: List[dict]) -> List[Site]:
    return [parse_site(site) for site in sites]


class AmberApi:
    def __init__(self, rest_client: RESTClientObject):
        self._rest_client = rest_client

    @staticmethod
    def create(configuration: Configuration):
        return AmberApi(RESTClientObject(configuration))

    def request(
        self,
        method,
        path,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        _preload_content=True,
        _request_timeout=None,
    ) -> RESTResponse:
        auth = self._rest_client.configuration.auth_settings()
        if "apiKey" in auth:
            token = auth["apiKey"]
            if headers is None:
                headers = {}
            headers[token["key"]] = token["value"]

        url = self._rest_client.configuration.host + path
        return self._rest_client.request(
            method,
            url,
            query_params,
            headers,
            body,
            post_params,
            _preload_content,
            _request_timeout,
        )

    def get_sites(self) -> List[Site]:
        response = self.request("GET", "/sites")
        if response.status == 200:
            return parse_sites(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)

    def get_current_price(
        self, site_id: str, **kwargs
    ) -> List[Union[ActualInterval, CurrentInterval, ForecastInterval]]:
        query_params = {}
        if "resolution" in kwargs:
            query_params["resolution"] = str(kwargs.get("resolution"))
        if "previous" in kwargs:
            query_params["previous"] = str(kwargs.get("previous"))
        if "next" in kwargs:
            query_params["next"] = str(kwargs.get("next"))

        response = self.request(
            "GET",
            "/sites/" + site_id + "/prices/current",
            None if query_params == {} else query_params,
        )

        if response.status == 200:
            return parse_intervals(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)

    def get_prices(
        self, site_id: str, **kwargs
    ) -> List[Union[ActualInterval, CurrentInterval, ForecastInterval]]:
        query_params = {}
        if "end_date" in kwargs:
            query_params["endDate"] = kwargs["end_date"].strftime(ISO_DATE_FORMAT)
        if "start_date" in kwargs:
            query_params["startDate"] = kwargs["start_date"].strftime(ISO_DATE_FORMAT)
        if "resolution" in kwargs:
            query_params["resolution"] = str(kwargs["resolution"])

        response = self.request(
            "GET",
            "/sites/" + site_id + "/prices",
            None if query_params == {} else query_params,
        )

        if response.status == 200:
            return parse_intervals(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)

    def get_usage(
        self, site_id: str, start_date: date, end_date: date, **kwargs
    ) -> List[Usage]:
        query_params = {
            "startDate": start_date.strftime(ISO_DATE_FORMAT),
            "endDate": end_date.strftime(ISO_DATE_FORMAT),
        }
        if "resolution" in kwargs:
            query_params["resolution"] = str(kwargs.get("resolution"))

        response = self.request("GET", "/sites/" + site_id + "/usage", query_params)

        if response.status == 200:
            return parse_intervals(json.loads(response.data.decode("utf-8")))
        else:
            raise ApiException(response.status, response.reason, response)
