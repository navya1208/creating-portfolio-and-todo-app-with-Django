from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

from to_do.models import *
# Create your views here.
def index(request):
    todos=To_do.objects.all()

    form=To_doForm()

    if request.method=='POST':
        form=To_doForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
        
    context={'todos':todos, 'form':form}
    return render(request,'to_do/list.html',context)


def update(request,pk):
    todo=To_do.objects.get(id=pk)

    form=To_doForm(instance=todo)
    if request.method=='POST':
        form=To_doForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'to_do/update.html',context)


def delete(request,pk):
    item=To_do.objects.get(id=pk)

    if request.method=="POST":
        item.delete()
        return redirect("/")

    context={'item':item}
    return render(request,'to_do/delete.html',context)
