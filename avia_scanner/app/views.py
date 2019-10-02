import time
import random
import re

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'
    context = {
        'form': SearchTicket(),
    }
    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""

    part_of_city = request.GET.get('term')  # получаем введеную подстроку
    pattern = f'^{part_of_city}.+'

    city_list = []
    if not cache.get('all_cities'):  # проверяем есть ли кэш, если нет(первый запуск) создаем и вносим туда все данные
        all_cities = list(City.objects.values('name'))  # запрашиваем сразу все, чтобы потом каждый раз не дергать базу
        cache.set('all_cities', all_cities, 300)

    for city in cache.get('all_cities'):
        match = re.findall(pattern, city['name'])
        if match:
            city_list.append(city['name'])

    if len(city_list) == 0:
        city_list.append('нет совпадений')

    results = city_list
    return JsonResponse(results, safe=False)
