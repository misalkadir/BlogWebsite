from django.urls import path
from .views import yazi_view, yaziEkle_view, yorumEkle_view, begen_view

app_name = "yazi"

urlpatterns = [
    path('yaziEkle', yaziEkle_view, name="yaziEkle"),
    path('yorumEkle', yorumEkle_view, name="yorumEkle"),
    path('begen/<str:id>', begen_view, name="begen"),

    path('<str:slug>', yazi_view, name="yazidetay"),
]
