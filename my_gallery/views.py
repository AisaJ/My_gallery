from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request,'home.html')


def image(request,category):
  try:
    image = Image.objects.get(category)
  except DoesNotExist:
    raise Http404()
  return render(request,'make-gallery/image.html',{'image':image})
