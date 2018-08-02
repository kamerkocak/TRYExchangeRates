import json
from urllib.request import urlopen

with urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=TRY&apikey=5Y57NAHCNN1GRX1O") as sterlingRequest:
    sterlingSource = sterlingRequest.read()
sterlingData = json.loads(sterlingSource)

def getSterlingName():
    sterlingName = sterlingData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    return sterlingName

def getSterlingTryRate():
    sterlingRate = sterlingData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return sterlingRate

def getSterlingRefTime():
    sterlingRefTime = sterlingData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

    return sterlingRefTime

