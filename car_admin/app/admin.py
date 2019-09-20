from django.contrib import admin
from django import forms
from .models import Car, Review, MAX_LENGTH
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    search_fields = ['car__model', 'title']   # поискать способ проще взаиодействия с данным полем
    list_display = ('car', 'title')
    actions = ['test_actions']
    list_filter = ('car', 'title')

    # как обратится к get_search_fields чтоб не срабатывало 2 раза
    # срабатывает 2 раза потому что дальше идет get_search_results, который его сова вызывает
    #
    def get_search_fields(self, request):
        """
        Return a sequence containing the fields to be searched whenever
        somebody submits a search query.
        """
        message = request.GET.get('q')
        self.message_user(request, "%s отправлено в поиск успешно." % message)
        return self.search_fields

    def test_actions(self, request, queryset):
        # print('====>>>>>', queryset)  # <QuerySet [<Review: Ford Mondeo IV Ford Mondeo Review>]>
        # print('====>>>>>', request)  # <WSGIRequest: POST '/admin/app/review/'>
        # print('====>>>>>', self)  # app.ReviewAdmin
        rows_select = queryset.values_list('title')
        message = "%s - that review selected" % rows_select
        self.message_user(request, "%s successfully." % message)
    test_actions.short_description = "test actions"


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
