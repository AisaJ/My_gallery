from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='galeria'),
  url(r'^image/(\d+)',views.image,name='image'),
  url(r'^search/',views.search_images,name='search_images'),
  url(r'^gallery/',views.gallery,name='gallery')
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)