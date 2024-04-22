

import http.client
import json
import login as l
import pandas as pd
import hashlib
from datetime import datetime




# creating json dump for chosen stock, exchange and timescale
def OHLC_func(interval,from_date,to_date,stock_code,exchange_code):
    conn = http.client.HTTPSConnection("api.icicidirect.com")
    payload = json.dumps({
        "interval": interval,
        "from_date": "2022-05-02T07:00:00.000Z",
        "to_date": "2022-05-03T07:00:00.000Z",
        "stock_code": "stock_code",
        "exchange_code": "exchange_code"
    })

    appkey = l.app_key
    secret_key = l.secret_key

    #checksum computation
    #time_stamp & checksum generation for request-headers
    time_stamp = datetime.utcnow().isoformat()[:19] + '.000Z'
    checksum = hashlib.sha256((time_stamp+payload+secret_key).encode("utf-8")).hexdigest()

    headers = {
        'Content-Type': 'application/json',
        'X-Checksum': 'token '+checksum,
        'X-Timestamp': time_stamp,
        'X-AppKey': appkey,
        'X-SessionToken': l.session_token
    }

    conn.request("GET", "/breezeapi/api/v1/historicalcharts", payload, headers)
    res = conn.getresponse()
    data = res.read()
    predfjson = data.decode("utf-8")
    df = pd.read_json('predfjson')


#Calculating the MACD of selected stock 
#MACD = 12-period closing price EMA – 26-period closing price EMA

def MACD(df,min_span,max_span,MACD_signal):

    dfMACD = df.copy()
    dfMACD['ema_min'] = dfMACD['close'].ewm(span = min_span).mean()
    dfMACD['ema_max'] = dfMACD['close'].ewm(span = max_span).mean()
    dfMACD['macd'] = dfMACD['ema_min'] - dfMACD['ema_max']
    dfMACD['macd_sig'] = dfMACD['macd'].ewm(span = MACD_signal).mean()
    dfMACD.dropna(inplace = True)
    
    return dfMACD

def main():
    pass
"""
awaiting values to pull to main function
OHLC_func(input from frontend)
MACD(df from OHLC_func)
"""

if __name__ == "__main__":
    main()