from attr import asdict
import pandas as pd
from stonk_structs import BUY, SELL, DIVIDENT
from stonk_names import *

# This is an example dataset, on how you can add the data. Check the BUY,SELL,DIVIDENT classes for waht each field means
transactions = [
    BUY(HTZ, 25.83, 7, '2020.06.08 16:15'),
    BUY(GE, 16.88, 2, '2020.06.08 16:11'),
    BUY(GE, 3.78, 0.45, '2020.06.08 17:44'),
    SELL(HTZ, 12.78, 7, '2020.06.11 15:50'),
    BUY(GE, 16.49, 2.2, '2020.06.11 20:56'),
    BUY(NIO, 43.41, 3, '2020.07.08 19:10'),
    DIVIDENT(GE, 0.004, '2020.07.28 07:24'),
    BUY(TSLA, 7.35, 0.005, '2020.08.04 20:47'),
    SELL(TSLA, 8.02, 0.005, '2020.08.13 15:31'),
    BUY(NKLA, 8, 0.20784619, '2020.08.24 15:54'),
    BUY(ZOOM, 40, 0.08948545, '2020.09.01 16:41'),
    BUY(SLACK, 25.89, 1, '2020.09.10 21:00'),
    SELL(NKLA, 6.98, 0.207846, '2020.09.16 19:26'),
    BUY(UPS, 50, 0.29, '2020.09.28 17:51'),
    BUY(AAL, 13.71, 1.000799, '2020.10.1 15:31'),
    BUY(BLIZ, 77.73, 0.9997, '2020.10.08 20:46'),
    BUY(AAL, 49.48, 4, '2020.10.14 21:58'),
    DIVIDENT(GE, 0.004, '2020.10.27 06:25'),
    SELL(AAL, 67.45, 5.000799, '2020.11.09 18:38'),
    BUY(PFIZER, 75, 1.8568, '2020.11.09 19:27'),
    SELL(PFIZER, 68.77, 1.8568, '2020.11.16 19:20'),
    SELL(SLACK, (36.19 - 0.22), 1, '2020.11.25 17:54'),
    SELL(ZOOM, 38.08, 0.08948545, '2020.11.25 17:58')
]

transaction_as_df = pd.DataFrame.from_records([asdict(t) for t in transactions])
transaction_as_df['date'] = pd.to_datetime(transaction_as_df['date'], format='%Y%m%d %H:%M')
transaction_as_df = transaction_as_df.set_index('date')