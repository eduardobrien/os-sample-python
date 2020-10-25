from flask import Flask
application = Flask(__name__)



# REQUIERE
# pip install finnhub-python
# pip install pandas


import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key="bpjqg37rh5re7t471mj0")

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
##print(res)


#Convert to Pandas Dataframe
import pandas as pd
#print(pd.DataFrame(res))



@application.route("/")
def hello():
#    return "Hello World! / Homa Mundo"
    return pd.DataFrame(res)

if __name__ == "__main__":
    application.run()
