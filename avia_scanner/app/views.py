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

    part_of_city = request.GET.get('term')
    pattern = f'^{part_of_city}.+'
    all_cities = list(City.objects.values('name'))
    city_list = []
    if not cache.get('all_cities'):
        cache.set('all_cities', all_cities, 300)
    else:
        for city in cache.get('all_cities'):
            match = re.findall(pattern, city['name'])
            if match:
                city_list.append(city['name'])
    results = city_list
    return JsonResponse(results, safe=False)
