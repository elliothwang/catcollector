from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('cats/', views.cats_index, name='index'),
  path('about/', views.about, name='about'),
  path('cats/<int:cat_id>', views.cats_detail, name='detail'),
  path('cats/create/', views.CatCreate.as_view(), name='cats-create'),
  path('cats/<int:pk>update/', views.CatUpdate.as_view(), name='cats-update'),
  path('cats/<int:pk>delete/', views.CatDelete.as_view(), name='cats-delete'),
]