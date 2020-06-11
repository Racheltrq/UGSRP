from django.conf.urls import url
from django.urls import include
from django.contrib import admin

from theory import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('theory.urls'))

]
