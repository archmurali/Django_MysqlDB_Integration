from rest_framework import serializers
from .models import OcCart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcCart
        fields = ["cart_id","product_id","customer_id","session_id"]