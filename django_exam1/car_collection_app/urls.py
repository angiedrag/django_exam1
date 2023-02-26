from django.urls import path, include

from django_exam1.car_collection_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue-page'),
    path('profile/', include([
        path('create/', views.profile_create, name='create-profile-page'),
        path('details/', views.profile_details, name='profile-details-page'),
        path('edit/', views.profile_edit, name='edit-profile-page'),
        path('delete/', views.profile_delete, name='delete-profile-page'),
    ])),
    path('car/', include([
        path('create/', views.car_create, name='create-car-page'),
        path('details/<int:id>', views.car_details, name='car-details-page'),
        path('edit/<int:id>', views.car_edit, name='edit-car-page'),
        path('delete/<int:id>', views.car_delete, name='delete-car-page'),
    ])),
]