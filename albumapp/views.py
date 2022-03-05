from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from matplotlib import image
from .models import *

# Create your views here.

# def hai(request):
#     return HttpResponse("<h2>hai</h2>")

def hai(request):
    return render(request, "albumapp/index.html") 

def view(request,pk):
    photos = Photo.objects.get(id=pk)
    
    context = {"photos":photos}
    return render(request, "albumapp/view.html", context)
    



def addphotos(request):
    category = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['Category_new'] != "":

            category, created = Category.objects.get_or_create(name=data['Category_new'])
        else:
            category= None

        photo = Photo.objects.create(
            category=category,
            description = data['DESCRIPTION'],
            image = image,
        ) 
        return redirect("gal")
    context = {"category":category}

    return render(request, "albumapp/addphoto.html", context)


def viewphoto(request ):
    
    photos = Photo.objects.all()
    
    context = {"photos":photos}

    return render(request, "albumapp/open.html", context, {'photos': photos})


def gallary(request):
    category = request.GET.get('category')
    
    if category == None:
       photos = Photo.objects.all()
    
    else:
        photos = Photo.objects.filter(category__name__contains=category)
   
    category = Category.objects.all()
    # photos = Photo.objects.all()


    context = {"category":category, "photos":photos}
    return render(request, 'albumapp/gallary.html', context)