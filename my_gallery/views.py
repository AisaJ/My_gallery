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

def search_images(request):
  if 'image' in request.GET and request.GET['image']:
    search_term = request.GET.get('image')
    searched_images = Image.search_by_category(search_term)
    searched_images2 = Image.search_by_location(search_term)
    message = f'{search_term}'

    return render(request,'make-gallery/search.html',{{"message":message, "images":search_images, "images":searched_images2}})

  else:
    message = "You haven't searched for any term."
    return render(request,'make-gallery/search.html',{{"message":message}})