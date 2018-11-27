from api import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('top/<int:age_range>/<int: income>/<int: amenity>', views.top_zipcode, name='top'),
    path('cluster/<str: zip_code>', views.same_cluster, name='cluster'),

]

