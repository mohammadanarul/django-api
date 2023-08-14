from django.urls import path
from apps.shop import views


urlpatterns = [
    path("create/", views.product_apiview),
    path("products/", views.product_fetch_apiview),
    path("products/<pk>/delete/", views.product_delete_apiview),
    path("products/<pk>/update/", views.product_update_apiview),
]
