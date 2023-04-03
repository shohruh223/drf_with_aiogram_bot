from rest_framework import serializers

from app.models import Product


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ()