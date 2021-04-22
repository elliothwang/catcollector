from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat

# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  # cats = Cat.objects.order_by('name')
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats' : cats})

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', { 'cat' : cat, 'feeding_form' : feeding_form})

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'

class CatUpdate(UpdateView):
  model = Cat
  # cannot edit name of cat bc it's omitted from fields attribute
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'