from django.shortcuts import render, redirect, HttpResponse, render_to_response
from .models import Course
from .forms import NewClass

def index(request):
    context = {
        "courses": Course.objects.all(),
        "form": NewClass(),
    }
    return render(request, "courses/index.html", context)

def add(request):
    form = NewClass(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            create = Course.objects.create(name = form.cleaned_data['name'], desc = form.cleaned_data['desc'])
            create.save()
            return redirect('/')
    context = {
        "courses": Course.objects.all(),
        "form": form,
    }
    return render(request, 'courses/index.html', context)

def remove(request, number):
    context = {
        'name': Course.objects.get(id=number).name,
        'desc': Course.objects.get(id=number).desc,
    }
    return render(request, "courses/remove.html", context)

def destroy(request, number):
    d = Course.objects.get(id=number)
    d.delete()
    return redirect('/')