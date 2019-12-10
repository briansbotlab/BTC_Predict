import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

# read file
file = pd.read_csv('binance_BTCUSDT_data.csv')



#print(file.dtypes)

# convert timestamp to datetime
file['Open_time'] = pd.to_datetime(file['Open_time'],unit='ms')

#print(file.dtypes)
#print(file.Open_time)


train_data = file[['Open_time','close']]
train_data = train_data.rename(columns={"Open_time": "ds", "close": "y"})


# 建立模型
model =Prophet()

model.fit(train_data)

#---------------
#預測
#---------------

# 建構預測集
future = model.make_future_dataframe(periods=100, freq='H') #forecasting .


# 進行預測
forecast = model.predict(future)
print('forecast..............................')
print(forecast.columns)
print(forecast)

figure=model.plot(forecast)

forecast.to_csv('forecast_BTCUSDT_data.csv', encoding='utf-8')

