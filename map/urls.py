from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^map$', views.gap_map, name='gap_map'),
    url(r'^get_map_data$', views.get_map_data, name='get_map_data'),
]
