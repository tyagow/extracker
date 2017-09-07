from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'core/index.html')


def valid_value(param, operation, value):
    print(param)
    if 'asks' in operation:
        return int(value) >= param[0]
    if 'bids' in operation:
        return int(value) < param[1]


def deep(request, operation, value):
    print(operation, value)
    import urllib.request, json
    with urllib.request.urlopen("https://www.mercadobitcoin.com.br/api/BTC/orderbook/") as url:
        data = json.loads(url.read().decode())

    index = 0
    total = 0.0
    operation_index = 1 if 'asks' in operation else 0
    total_btc = 0
    while True:
        if 'asks' in operation and int(value) >= data[operation][index][0]:
            total += data[operation][index][1]
            print(data[operation][index][0], value, total)
            index += 1
        elif 'bids' in operation:

            if int(value) > total_btc:
                total += data[operation][index][0] * data[operation][index][1]
                total_btc += data[operation][index][1]
                print(data[operation][index][1], value, total, total_btc)
                index += 1
            else:
                total = total / float(total_btc)
                operation = ''

        else:
            return HttpResponse(total)


