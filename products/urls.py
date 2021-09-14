from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductPageView.as_view(), name='list'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
]


