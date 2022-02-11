import re
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password'],
        )
        msg="User is Created"
        uid=User.objects.all()
        return render(request,'index.html',{'msg':msg,'uid':uid})
    uid=User.objects.all()
    return render(request,'index.html',{'uid':uid})

def edit(request,pk):
    uid=User.objects.get(id=pk)
    if request.method=='POST':
        uid.name=request.POST['name']
        uid.email=request.POST['email']
        uid.phone=request.POST['phone']
        uid.password=request.POST['password']
        uid.save()
        return redirect('index')
    return render(request,'edit.html',{'uid':uid})


def delete(request,pk):
    uid=User.objects.get(id=pk)
    uid.delete()
    return redirect('index')