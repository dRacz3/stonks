import pandas as pd
import yfinance as yf
from exchangeratesapi import Api as exchangeApi


def get_stock_current_value(stonk_name):
    stonk = yf.Ticker(stonk_name)
    # get historical market data, here max is 5 years.
    return stonk.history(period="max").iloc[-1]['Close']


def get_huf_to_usd_exchange_rate_in_interval(start, stop):
    api = exchangeApi()
    huf_to_usd = pd.DataFrame.from_records(api.get_rates('USD',
                                                         ['HUF'],
                                                         start_date=start,
                                                         end_date=stop)[
                                               'rates']).transpose()
    huf_to_usd.index = pd.to_datetime(huf_to_usd.index)
    huf_to_usd.index.name = 'date'
    return huf_to_usd
