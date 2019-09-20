from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")
    # Х = (стоимость + стоимость * процентную ставку) / срок    в    месяцах

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if not rate or rate < 0 or rate > 100:
            raise forms.ValidationError("Процентная ставка не может быть отрицательной или больше 100")
        return rate

    def clean_months_count(self):
        months_count = self.cleaned_data.get('months_count')
        if not months_count or months_count < 0:
            raise forms.ValidationError("Количество месяцев не может быть отрицательным")
        return months_count

    def clean(self):
        # общая функция валидации
        # как я понял он просто запускает  to_python(), validate(), run_validators()
        # И его переопределять не надо

        # попытка избавиться от повторений, почему-то пропадает cleaned_data
        # cleaned_data = super().clean()
        # initial_fee = cleaned_data.get('initial_fee')
        # rate = cleaned_data.get('rate')
        # months_count = cleaned_data.get('months_count')
        # if not initial_fee or months_count or rate < 0:
        #     raise forms.ValidationError("Значение не может быть отрицательным")

        return self.cleaned_data
