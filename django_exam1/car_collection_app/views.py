from django_exam1.car_collection_app import models, forms
from django.shortcuts import render, redirect

from django_exam1.car_collection_app import models
from django_exam1.car_collection_app.models import Profile, Car
from django_exam1.car_collection_app.forms import ProfileForm, CarForm, ProfileEditForm


def home_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name="index.html", context=context)

def catalogue_page(request):
    cars = Car.objects.all()
    context = {'profile': Profile.objects.first(), 'cars': cars}

    return render(request, template_name="catalogue.html", context=context)


def create_profile_page(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = forms.ProfileForm()

    context = {'form': form}

    return render(request, template_name="create-profile.html", context=context)


def profile_details_page(request):
    profile = Profile.objects.first()
    all_cars = Car.objects.all()
    total_sum = sum(car.price for car in all_cars)
    context = {'profile': profile, 'total_sum': total_sum}

    return render(request, template_name="profile-details.html", context=context)


def edit_profile_page(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {'form': ProfileEditForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')
        else:
            context = {'profile': Profile.objects.first(), 'form': form}
            return render(request, "edit-profile.html", context)


def delete_profile_page(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()

        return redirect('home')

    return render(request, 'delete-profile.html', {"profile": Profile.objects.first()})


def create_car_page(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('catalogue')

    context = {'profile': Profile.objects.first(), 'form': form}

    return render(request, template_name="create-car.html", context=context)


def car_details_page(request, pk):
    car = Car.objects.get(id=pk)
    context = {'profile': Profile.objects.first(), 'car': car}

    return render(request, template_name="car-details.html", context=context)


def edit_car_page(request, pk):
    car = Car.objects.get(id=pk)

    if request.method == "GET":
        context = {'profile': Profile.objects.first(), 'form': CarForm(initial=car.__dict__)}
        return render(request, "edit-car.html", context)
    else:
        form = CarForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'profile': Profile.objects.first(), 'form': form}
            return render(request, "edit-car.html", context)


def car_delete(request, pk):
    car = models.Car.objects.get(id=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = forms.DeleteCarForm(instance=car)
    context = {'profile': Profile.objects.first(), 'form': form}
    return render(request, "delete-car.html", context=context)
