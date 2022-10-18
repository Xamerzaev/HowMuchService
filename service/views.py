from django.shortcuts import render

# https://www.ozon.ru/
# https://www.wildberries.ru/
# https://www.dns-shop.ru/
# https://www.eldorado.ru
# https://aliexpress.ru/
# https://www.mvideo.ru/
# http://www.sotovik.ru/


def index(request):
    return render(request, 'index.html', context={})
