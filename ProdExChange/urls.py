from django.contrib import admin
from django.urls import path
from ProdExChange import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('add/', views.add, name='add'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),


]
