from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from . import models


# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {
        'all_cars': all_cars
    }
    return render(request, 'cars/list.html', context=context)

def add(request):
    if request.method == 'POST':
        models.Car.objects.create(
            brand=request.POST['brand'],
            year=int(request.POST['year']),
        )
        # if user submits the form, redirect to the list page
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.method == 'POST':
        pk=request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except Exception as e:
            print(e)
    else:
        return render(request, 'cars/delete.html')
