from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^theory/(\d+)/$', views.key_detail, name='key_detail'),
    url(r'^theory/(\d+)/common/', views.common, name='common'),
    url(r'^theory/(\d+)/notcommon/', views.notcommon, name='notcommon')
]
