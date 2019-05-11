from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='galeria'),
  url(r'^image/(\d+)',views.image,name='image'),
  url(r'^gallery/',views.gallery,name='gallery')
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)