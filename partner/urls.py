from django.conf.urls import url, include
from .views import signup

urlpatterns = [
    url(r'^$', signup, name="signup"),
]
