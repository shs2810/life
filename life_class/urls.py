from django.conf.urls import url
from . import views
urlpatterns = [
    ##life_class
    url(r'^$', views.life_class, name ='life_class'),

    ##life_class_detail
    url(r'^life_class/(?P<pk>\d+)/$', views.life_class_detail, name='life_class_detail'),
    # ^ - 시작
    # (?P<pk>[0-9]+) 장고가 pk 변수에 모든 값을 넣어 뷰로 전송한다 [0-9] 은 문자를 제외한 0~9중 한 가지 숫자만 온다는 뜻. + 는 그 이상의 숫자가 올 수 있다는 뜻
    # $ - 마지막, 그 뒤로 문자가 더 오면 안된다.
    # ex) 127.0.0.1:8000/life_class_detail/5/ 이면 life_calss_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달
    ##life_class_write
    url(r'^life_class/life_class_write/$', views.life_class_write, name='life_class_write'),
    url(r'^create/$', views.create, name='create'),

]