from requests import get, utils
from decimal import Decimal

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency(code):
    text = response.split("Valute ID=")
    for i in text:
        if code.upper() in i:
            # print(code.upper(), end=" ")
            return Decimal(i.replace("/", "").split("Value")[-2].replace(",", "."))

print(currency("uSd"))
print(currency("EUR"))
