import json
from urllib.request import urlopen

with urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=TRY&apikey=5Y57NAHCNN1GRX1O") as euroRequest:
    euroSource = euroRequest.read()
euroData = json.loads(euroSource)

def getEuroName():
    euroName = euroData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    return euroName

def getEuroTryRate():
    euroRate = euroData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return euroRate
