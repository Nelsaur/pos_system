from rest_framework import serializers
from menu.models import Item, Order

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"