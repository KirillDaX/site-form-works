from django import forms
from .models import Review

from ckeditor.widgets import CKEditorWidget


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label='Текст обзора')

    class Meta:
        model = Review
        fields = ['car', 'title', 'text']
