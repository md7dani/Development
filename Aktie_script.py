import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'BDP5P3C3IZO7JN21'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval ='1min', outputsize = 'full')
print(data)