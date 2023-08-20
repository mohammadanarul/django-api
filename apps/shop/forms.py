from django import forms
from apps.shop.models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("created_at", "updated_at")
