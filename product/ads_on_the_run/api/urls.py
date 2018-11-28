from api import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('getConstCode', views.get_const_code),

    # path('top/', views.tmp),
    path('top/<int:age_range>/<int:income>/<int:amenity>', views.top_zip_code, name='top'),
    path('cluster/<str:zip_code>', views.same_cluster, name='cluster'),

]

