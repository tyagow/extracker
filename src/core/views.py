from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'core/index.html')


def valid_value(param, operation, value):
    if 'asks' in operation:
        return int(value) >= param[0]
    if 'bids' in operation:
        return int(value) < param[0]


def deep(request, operation, value):
    print(operation, value)
    import urllib.request, json
    with urllib.request.urlopen("https://www.mercadobitcoin.com.br/api/BTC/orderbook/") as url:
        data = json.loads(url.read().decode())

    index = 0
    btc_total = 0.0
    while True:
        if valid_value(data[operation][index], operation, value):
            btc_total += data[operation][index][1]
            print(data[operation][index][0], value, btc_total)
            index +=1
        else:
            return HttpResponse(btc_total)
    return HttpResponse(data[operation])


