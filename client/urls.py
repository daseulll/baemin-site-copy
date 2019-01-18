from django.conf.urls import url, include
from .views import (
    index, signup, login, order
)


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^login/$', login, name="login"),
    url(r'^(?P<partner_id>\d+)/$', order, name="order"),

]
