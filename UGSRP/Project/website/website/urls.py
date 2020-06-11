from django.conf.urls import url
from django.contrib import admin

from theory import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^theory/(\d+)/$', views.key_detail, name='key_detail'),
    url(r'^theory/(\d+)/common/', views.common, name='common'),
    url(r'^theory/(\d+)/notcommon/', views.notcommon, name='notcommon')
]
