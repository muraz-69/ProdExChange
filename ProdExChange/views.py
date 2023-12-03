from django.shortcuts import  render, redirect
from .models import User, Products
from ProdExChange.forms import ProductForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = User(firstname=request.POST.get('firstname', ''), lastname=request.POST.get('lastname', ''),
                      email=request.POST.get('email', ''),
                      username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def index(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('username', ''),
                               password=request.POST.get('password', '')).exists():
            member = User.objects.filter(username=request.POST.get('username', ''),
                                         password=request.POST.get('password', ''))
            return render(request, 'index.html', {'member': User})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductForm()
        return render(request, 'addproducts.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def products(request):
    return render(request, 'products.html')


def show(request):
    products = Products.objects.all()
    return render(request, 'show.html', {'Products': products})


def delete(request,id):
    product=products.objects.get(id=id)
    product.delete()
    return redirect('/show')


def edit(request,id):
    products = Products.objects.get(id=id)
    return render(request,'edit.html',{'Products':products})
