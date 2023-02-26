from django.urls import path, include

from django_exam1.car_collection_app.views import home_page, create_profile_page, edit_profile_page, \
    delete_profile_page, profile_details_page, catalogue_page, create_car_page, edit_car_page, car_details_page, \
    delete_car_page

urlpatterns = [
    path('', home_page, name='home'),
    path('create/', create_profile_page, name='create-profile'),
    path('edit/', edit_profile_page, name='edit-profile'),
    path('delete/', delete_profile_page, name='delete-profile'),
    path('details/', profile_details_page, name='profile-details'),
    path('catalogue/', catalogue_page, name='catalogue'),
    path('create/', create_car_page, name='create-car'),
    path('<int:pk>/edit/', edit_car_page, name='edit-car'),
    path('<int:pk>/delete/', delete_car_page, name='delete-car'),
    path('<int:pk>/details/', car_details_page, name='car-details'),
]