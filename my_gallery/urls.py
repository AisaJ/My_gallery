from django.conf.urls import url
from . import views

urlpatterns=[
  url(r'^$',views.home,name='galeria'),
  url(r'^image(categry)',views.image,name='image')
]