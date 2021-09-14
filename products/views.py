from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Category, Product

# Create your views here.
class ProductPageView(ListView):
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(is_available=True)



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = "product"

