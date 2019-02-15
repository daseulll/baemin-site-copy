from django.conf.urls import url, include
from .views import (
    index, signup, login, order, order_list, contact
)


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^login/$', login, name="login"),
    url(r'^(?P<partner_id>\d+)/$', order, name="order"),
    url(r'^order/$', order_list, name="order_list"),
    url(r'^contact/$', contact, name="contact"),

]
