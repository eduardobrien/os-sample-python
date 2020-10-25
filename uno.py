dias_atras = 30
# GGAL GGAL.BA TSLA MSFT AAPL
papel = 'AAPL'

import yfinance as yf
from datetime import date, datetime, timedelta
tomorrow = date.today() + timedelta(days=1)
inicio = date.today() - timedelta(days=dias_atras)

#define the ticker symbol
# GGAL TSLA 
tickerSymbol = papel

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=inicio, end=tomorrow)

#see your data
print(tickerDf)

