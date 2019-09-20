from django.forms import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm
    context = {
        'form': form,
        'product': product
    }
    user_id_session = request.session['_auth_user_id']
    if product.id not in request.session['reviewed_products']:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            request.session['reviewed_products'].append(product.id)
            if form.is_valid():
                text = form.cleaned_data['text']
                product = Product(id=pk)
                review = Review(text=text, product=product)
                review.save()
                context['is_review_exist'] = True

        if request.method == 'GET':
            if product.id in request.session['reviewed_products']:
                context['is_review_exist'] = True
            reviews = Review.objects.filter(product__id=pk)
            context['reviews'] = reviews

    else:
        context['is_review_exist'] = True

    context['test'] = request.session.items()
    reviews = Review.objects.filter(product__id=pk)
    context['reviews'] = reviews
    return render(request, template, context)
