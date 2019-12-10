import numpy as np
import pandas as pd
from binance.client import Client
api_key = 'your_api_key'
api_secret = 'your_api_secret'
client = Client(api_key, api_secret)

klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1HOUR, '30 days ago UTC')
whole_df = pd.DataFrame(klines)
whole_df.columns = ['Open_time',
                    'open',
                    'high',
                    'low',
                    'close',
                    'volume',
                    'Close_time',
                    'Quote asset volume',
                    'number of trades',
                    'Taker buy base asset volume',
                    'Taker buy quote asset volume',
                    'Ignore']
whole_df = whole_df[['Open_time', 'open', 'high', 'low', 'close', 'volume']]
whole_df = whole_df.drop_duplicates(subset=['Open_time'], keep=False)
#whole_df = whole_df.convert_objects(convert_numeric=True)
whole_df.to_csv('binance_BTCUSDT_data.csv', encoding='utf-8')