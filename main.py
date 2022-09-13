from tracemalloc import start
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
import pandas_datareader as web
import datetime as date
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM

AAPL_TICKER = 'AAPL'
TSLA_TICKER = 'TSLA'

company = AAPL_TICKER
start = date.datetime(2020, 7, 7)
today = date.datetime.today()
data = web.DataReader(company, 'yahoo', start, today)
data_after_close = data['Close']

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data_after_close.values.reshape(-1,1))

print(scaled_data)