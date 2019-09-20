from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    #  формула из задания Х = (стоимость + стоимость * процентную ставку) / срок    в    месяцах
    form = CalcForm(request.GET)
    context = {
        'form': form,
        }
    if form.is_valid():
        result = (form.cleaned_data['initial_fee'] + form.cleaned_data['initial_fee'] * form.cleaned_data['rate'])\
                 / form.cleaned_data['months_count']
        common_result = result * form.cleaned_data['months_count']
        context.update({'result': result,
                        'common_result': common_result
                        })
    return render(request, template, context)
