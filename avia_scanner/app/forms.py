from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city = City.objects.all()
    departure_city = forms.CharField(widget=AjaxInputWidget('api/city_ajax', attrs={'class': 'inline right-margin'}),
                                     label='Город отправления')
    arrival_city = forms.ModelChoiceField(queryset=city, to_field_name='name', label='Город прибития')
    date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta(object):
        model = City

