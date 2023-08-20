from django.shortcuts import render, redirect
from apps.shop.forms import ProductForm
from apps.shop.models import Product


def product_list_view(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}
    return render(request, "products/list.html", context)


def product_create_view(request):
    form = ProductForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "products/create.html", context)
