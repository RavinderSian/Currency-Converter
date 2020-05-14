import xml.etree.ElementTree as ET

def getData():
    tree = ET.parse("euro.xml")
    root = tree.getroot()
    currencyList = []
    for child in root:
        item = {"currency":child.attrib['currency'], "rate":child.attrib['rate']}
        currencyList.append(item)

    currencies = []
    euroRates = []
    for entry in currencyList:
        currencies.append(entry['currency'])
        euroRates.append(entry['rate'])
        exchangeRates = dict(zip(currencies, euroRates))
    return exchangeRates

def currencyConversion():
    rates = getData()
    currencyAbbrevations = rates.keys()

    if (givenCurrency in currencyAbbrevations) and (desiredCurrency in currencyAbbrevations):
        givenRate = float(rates[givenCurrency])
        givenAmountInEuros = moneyToConvert/givenRate

        targetRate = float(rates[desiredCurrency])
        amountDesiredCurrency = round(givenAmountInEuros*targetRate,2)

        print("We have converted {} {}".format(moneyToConvert, givenCurrency))
        print("To {} {}".format(desiredCurrency, amountDesiredCurrency))

    else:
        print("Conversion not possible, currency not found")

converting = True
while converting == True:
    givenCurrency = input("What currency would you like to convert? (format: GBP)").upper()
    desiredCurrency = input("What currency do you want to convert to? (format: GBP)").upper()
    amount = input("How much would you like to convert?")
    moneyToConvert = abs(float(amount))
    getData()
    try:
        currencyConversion()
    except:
        if Exception:
            print("Enter numerical value as amount!")
    moreConversion = input("Would you like to perform another conversion? Yes or No").upper()
    if moreConversion == "NO":
        converting = False
    elif moreConversion == "YES":
        continue
