import requests

api_key = 'F8CvWt7D883XszhAKhTAgX4NNi8AwtJ3'


def get_currency(display_currency, base_currency):  # имена валют
    """Курс валюты-1 к валюте-2"""

    # входные параметры
    # display_currency = "RUB"
    # base_currency = "EUR"

    # ответ сервиса
    # {
    #     "success": true,
    #     "timestamp": 1668960243,
    #     "base": "EUR",
    #     "date": "2022-11-20",
    #     "rates": {
    #         "RUB": 62.952736
    #     }
    # }

    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={display_currency}&base={display_currency}"
    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    return result  # курс валюты


def convert_currency(from_currency, amount, to_currency):  # имена валют
    """Перевести количетсво валюты-1 к валюте-2 """

    # входные параметры
    # from_currency = "USD"
    # amount = "2509"
    # to_currency = "RUB"

    # ответ сервиса
    # {
    #     "success": true,
    #     "query": {
    #         "from": "RUB",
    #         "to": "USD",
    #         "amount": 1
    #     },
    #     "info": {
    #         "timestamp": 1668951303,
    #         "rate": 0.016434
    #     },
    #     "date": "2022-11-20",
    #     "result": 0.016434
    # }

    # https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount=1
    URL = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        "apikey": api_key,
    }

    response = requests.request("GET", URL, headers=headers)

    status_code = response.status_code
    result = response.text

    return result  # курс валюты

# TODO это заглушка
def convert_currency(from_currency, amount, to_currency):  # имена валют
    """Заглушка"""

    temp = dict()
    temp['result'] = 1
    return temp.get('result')