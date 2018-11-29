from api.views import filter_zip_code, home, kiosk_zip_code, sports_detail
from django.urls import path


urlpatterns = [
    path('', home.index, name='index'),

    path('filter/<int:age_range>/<int:income>/<int:amenity>', filter_zip_code.index, name='filter'),
    path('cluster/<str:zip_code>', kiosk_zip_code.index, name='kiosk'),
    path('sports/<str:zip_code>', sports_detail.index, name='sports')
]

