from django.urls import path
from ci_order import views
urlpatterns = [
    path('place_order/',views.place_order, name = 'place_order')
]