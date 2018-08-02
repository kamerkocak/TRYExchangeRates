from DollarTry import *
from EuroTry import *
from SterlingTry import *

def showMe():
    print("USD/TRY: " + str(getDollarTryRate()) + " As Of : " + str(getDolarRefTime()) + " UTC (tsi -3)")
    print("EUR/TRY: " + str(getEuroTryRate()) + " As Of : " + str(getEuroRefTime()) + " UTC (tsi -3)")
    print("GBP/TRY: " + str(getSterlingTryRate()) + " As Of : " + str(getSterlingRefTime()) + " UTC (tsi -3)")
