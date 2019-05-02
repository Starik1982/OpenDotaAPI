from django.conf.urls import url, include
from main import views



urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^get_json/$', views.get_update, name='get_json'),

]