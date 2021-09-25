from django.shortcuts import render, redirect
from cart.cart import Cart

# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import OrderCreateForm
from .models import Item, Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = '/'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            for c in request.session['cart'].values():
                Item.objects.create(
                    order=form,
                    product=c['name'],
                    price=c['price']
                )
        return redirect(reverse('page:index'))



