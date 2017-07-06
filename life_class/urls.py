from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.life_class, name ='life_class'),
    url(r'^life_class_detail/$', views.life_class_detail, name='life_class_detail'),
    url(r'^life_class_write/$', views.life_class_write, name='life_class_write'),
]