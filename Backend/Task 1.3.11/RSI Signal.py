import pandas as pd
from smartapi.smartConnect import SmartConnect

# Create a SmartConnect object
obj = SmartConnect(api_key="your_api_key")

def OHLCHistory(symbol, token, interval, fdate, todate):
    """Function to fetch OHLC history data"""
    try:
        historicParam = {
            "exchange": "NSE",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "interval": interval,
            "fromdate": fdate,
            "todate": todate
        }
        # Fetch the historical data
        history = obj.getCandleData(historicParam)['data']
        history = pd.DataFrame(history)
        # Rename the columns
        history = history.rename(
            columns = {0: "Datetime", 1: "open", 2: "high", 3: "low", 4: "close", 5: "volume"})
        # Convert the 'Datetime' column to datetime type
        history['Datetime'] = pd.to_datetime(history['Datetime'])
        # Set the 'Datetime' column as the index
        history = history.set_index('Datetime')

        return history
    except Exception as e:
        print("Api failed: {}".format(e))

def RSI(df, window):
    """Function to calculate RSI"""
    delta = df['close'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.ewm(span=window, adjust=False).mean()
    average_loss = abs(down.ewm(span=window, adjust=False).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Fetch the OHLC history data
df = OHLCHistory('NIFTY', 'your_token', 'your_interval', 'your_from_date', 'your_to_date')

# Calculate the RSI
df['RSI'] = RSI(df, 14)

print(df)