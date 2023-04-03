from django.urls import path
from app.views import ProductView


urlpatterns = [
    path('', ProductView.as_view(), name="product")
]