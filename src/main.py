"""Module for FastAPI demo"""
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def index():
    """
    Returns HTML home page with link to documentation
    """
    with open("templates/home.html", encoding="utf-8") as home_file:
        home_page = home_file.read()

    return HTMLResponse(content=home_page)


@app.get("/exchange-rates")
async def exchange_rates() -> dict:
    """
    Returns exchange rates from static file data/exchange_rates.json
    :returns    exchange_rates_dict
    :rtype:                         dict
    """

    with open("data/exchange_rates.json", encoding="utf-8") as exch_rate_file:
        exchange_rates_dict = json.load(exch_rate_file)

    return exchange_rates_dict


@app.get("/exchange-rates/{currency}")
async def exchange_rate_single(currency: str) -> dict:
    """
    Returns exchange rate for specific currency from static file
    data/exchange_rates.json
    :type       currency:           str
    :returns    exchange_rates_dict
    :rtype:                         dict
    """
    exchange_rate = {}
    with open("data/exchange_rates.json", encoding="utf-8") as exch_rate_file:
        exchange_rates_dict = json.load(exch_rate_file)

    for currency_name, rate in exchange_rates_dict["data"].items():
        if currency_name == currency:
            exchange_rate[currency] = rate

    return exchange_rate
