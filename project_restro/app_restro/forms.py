from .models import Category, Menu
from django import forms


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Category


class MenuCreateForm(forms.ModelForm):
    # fields = "__all__"
    class Meta:
        fields = ("menu_title", "category_id", "menu_desc", "menu_ingredient", "menu_img", "menu_price")
        model = Menu
