from django.urls import path
from . import api

app_name = 'mysite'
urlpatterns = [
    path('city/', api.City.as_view()),
    path('city/<int:city_id>/street/', api.Street.as_view()),
    path('shop/?street=&city=&open=', api.Shop.as_view()),
    path('shop/', api.Shop.as_view()),

]