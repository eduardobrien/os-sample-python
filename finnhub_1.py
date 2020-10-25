import finnhub

#https://github.com/Finnhub-Stock-API/finnhub-python

# Configure API key
configuration = finnhub.Configuration(
    api_key={
        'token': 'bpjqg37rh5re7t471mj0' # Replace this
    }
)

finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))

# Stock candles
#print(finnhub_client.stock_candles('AAPL', 'D', 1594673621, 1594673621))
print(finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249))

# Aggregate Indicators
#print(finnhub_client.aggregate_indicator('AAPL', 'D'))

# Basic financials
#print(finnhub_client.company_basic_financials('AAPL', 'margin'))

# Earnings surprises
#print(finnhub_client.company_earnings('TSLA', limit=5))