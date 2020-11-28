import pandas as pd
from retireve_data import get_huf_to_usd_exchange_rate_in_interval, get_stock_current_value
from transactions import transaction_as_df as transaction_df

pd.options.mode.chained_assignment = None  # default='warn'

# Load historical huf->usd data for the the traded intervals
huf_to_usd = get_huf_to_usd_exchange_rate_in_interval(start=str(transaction_df.index[0].date()),
                                                      stop=str(transaction_df.index[-1].date()))

# Combine them with the earnings by date.
transations_with_usd = pd.merge_asof(transaction_df.sort_index(), huf_to_usd, left_on='date', right_on='date')
transations_with_usd['prince_in_HUF_on_transaction_day'] = transations_with_usd['price'] * transations_with_usd['HUF']
current_earnings = transaction_df.groupby(['stonk_name']).sum().round(decimals=4)

def update_stock_value(row):
    return get_stock_current_value(row.name)


def calc_profit(row):
    return (row.current_price * row.amount) + row.price


def calculate_acitve_investment_value():
    active_investments = current_earnings[current_earnings['amount'] > 0.001]
    active_investments['current_price'] = active_investments.apply(update_stock_value, axis=1)
    active_investments['current_profit'] = active_investments.apply(calc_profit, axis=1)
    return active_investments.current_profit.sum(), active_investments


print(calculate_acitve_investment_value())