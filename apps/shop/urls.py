from django.urls import path
from apps.shop import views


urlpatterns = [
    path("", views.product_list_view, name="product_list"),
    path("products/create/", views.product_create_view, name="product_create"),
]
