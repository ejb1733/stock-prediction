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