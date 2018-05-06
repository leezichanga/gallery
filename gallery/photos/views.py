from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the My Gallery')

def my_gallery(request):
    photos = Photos.objects.all()
    return render(request, 'gallery.html', {'photos':photos})
