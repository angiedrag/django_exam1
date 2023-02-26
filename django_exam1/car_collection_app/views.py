from django_exam1.car_collection_app import models, forms
from django.shortcuts import render, redirect

from django_exam1.car_collection_app import models
from django_exam1.car_collection_app.models import Profile, Car
from django_exam1.car_collection_app.forms import ProfileForm, CarForm


def index(request):
    profile = models.Profile.objects.first()
    context = {'profile': profile}
    return render(request, template_name="car_collection_app/index.html", context=context)


def car_create(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = forms.CarForm
    context = {'form': form}
    return render(request, template_name="car_collection_app/car-create.html", context=context)


def car_delete(request, car_id):
    car = models.Car.objects.get(id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = forms.DeleteCarForm(instance=car)
    context = {'form': form}
    return render(request, template_name="car_collection_app/car-delete.html", context=context)


def car_details(request, car_id):
    car = models.Car.objects.get(id=car_id)
    context = {'car': car}
    return render(request, template_name="car_collection_app/car-details.html", context=context)


def car_edit(request, car_id):
    car = models.Car.objects.get(id=car_id)
    if request.method == "GET":
        context = {'form': forms.CarForm(initial=car.__dict__)}
        return render(request, template_name=("car_collection_app/car-edit.html", context))
    else:
        form = forms.CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, template_name=("car_collection_app/car-edit.html", context))



def catalogue(request):
    cars = models.Car.objects.all()
    all_cars = 0
    for car in cars:
        all_cars += 1
    context = {'cars': cars, 'all_cars': all_cars}

    return render(request, template_name="car_collection_app/catalogue.html", context=context)


def profile_create(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = forms.ProfileForm()
    context = {'form': form}
    return render(request, template_name="car_collection_app/profile-create.html", context=context)


def profile_delete(request):
    profile = models.Profile.objects.first()
    cars = models.Car.objects.all()
    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('index')

    return render(request, template_name="car_collection_app/profile-delete.html")


def profile_details(request):
    profile = models.Profile.objects.first()
    all_cars = models.Car.objects.all()
    total_cars = len(all_cars)
    try:
        average_rating = sum(game.rating for game in all_cars) / total_cars
    except ZeroDivisionError:
        average_rating = 0
    context = {'profile': profile, 'total_cars': total_cars, 'average_rating': average_rating}

    return render(request, template_name="car_collection_app/profile-details.html", context=context)


def profile_edit(request):
    profile = models.Profile.objects.first()
    if request.method == "GET":
        context = {'form': forms.ProfileEditForm(initial=profile.__dict__)}
        return render(request, 'car_collection_app/profile-edit.html', context)
    else:
        form = forms.ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details-page')
        else:
            context = {'form': form}
            return render(request, template_name="car_collection_app/profile-edit.html", context=context)

    return render(request, template_name="car_collection_app/profile-edit.html")
