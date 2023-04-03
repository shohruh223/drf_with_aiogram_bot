from rest_framework.generics import ListCreateAPIView

from app.models import Product
from app.serializers import ProductSerializers


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
