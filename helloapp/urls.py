from django.conf.urls import url
from .views import ListSongsView, MyView


urlpatterns = [
    url(r'^v1/cart', ListSongsView.as_view(), name="cart"),
    url(r'^mine/$', MyView.as_view(), name='my-view'),
]