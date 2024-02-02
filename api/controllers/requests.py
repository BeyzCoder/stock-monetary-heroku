from api.models.parameters import PathParam, StatementQuery, QuoteQuery
from api.utils.parsing import parse_statement, parse_quota
from urllib.error import HTTPError
from typing import Dict
import requests as req
import os
import json


def grab_enviro_key(key: str) -> str:
    """
    TODO
    """

    api_website = os.getenv(key)

    # Check if the variable is in the environment.
    if api_website is None:
        raise ValueError("The api key has not been set up yet in the server environment.")

    return api_website


def fetch_text(url: str, **kwargs: Dict) -> str:
    """
    Send out a request get to the url.

    @param url: The url that will be send out a request.
    @return: response text of the request.
    """

    packet_request = {"params" : {}, "headers" : {}}
    if "params" in kwargs and "headers" in kwargs:
        packet_request["params"] = kwargs["params"]
        packet_request["headers"] = kwargs["headers"]

    resp = req.get(url, **packet_request)

    if resp.status_code != 200:
        raise HTTPError(resp.url, resp.status_code, "", resp.headers, None)

    return resp.text


def fetch_statement(path: PathParam, query: StatementQuery, route_key: str) -> Dict:
    """
    TODO
    """

    try:
        # Get the proper api website for the statement.
        api_website = grab_enviro_key(route_key)
    except ValueError as err:
        return str(err)

    if query.freq == "quarterly":
        api_website = api_website + "quarterly/"

    api_website = api_website.format(path.symbol)

    try:
        # Get the text data.
        text_data = fetch_text(api_website)
    except HTTPError as err:
        return str(err)

    financial_statement = parse_statement(text_data)

    return financial_statement


def fetch_quote(path: PathParam, query: QuoteQuery, route_key: str) -> Dict:
    """
    TODO
    """

    try:
        # Get the proper api website for the statement.
        api_website = grab_enviro_key(route_key)
        headers = json.loads(grab_enviro_key("CUSTOM_HEADER"))
    except ValueError as err:
        return str(err)

    api_website = api_website.format(path.symbol)

    try:
        # Get the text data.
        text_data = fetch_text(api_website, params=query.__dict__, headers=headers)
    except HTTPError as err:
        return str(err)

    quote_data = parse_quota(text_data)

    return quote_data
