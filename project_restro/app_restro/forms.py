from .models import Category, Menu
from django import forms


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Category


class MenuCreateForm(forms.ModelForm):
    # fields = "__all__"
    class Meta:
        exclude = ['menu_img']
        fields = ("menu_title", "category_id", "menu_desc", "menu_ingredient", "menu_price")
        model = Menu
