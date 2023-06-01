from rest_framework.serializers import Serializer
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from app_restro.models import Category, Menu


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("category_name",)
        model = Category


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "menu_title", "category_id", "menu_desc", "menu_price", "menu_ingredient")
        model = Menu
