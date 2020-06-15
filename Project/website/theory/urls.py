from django.conf.urls import url
from theory import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^theory/(\d+)/$", views.key_detail, name="key_detail"),
    url(
        r"^theory/(\d+)/toggle_common/(\d)/", views.toggle_common, name="toggle_common"
    ),
]
