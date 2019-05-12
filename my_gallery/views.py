from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def home(request):
  return render(request,'home.html')

def gallery(request):
  all_images = Image.objects.all()
  return render(request,'make-gallery/gallery.html',{'all_images': all_images})

def image(request,image_id):
  try:
    image = Image.objects.get(id=image_id)
  except DoesNotExist:
    raise Http404()
  return render(request,'make-gallery/image.html',{'image':image})
