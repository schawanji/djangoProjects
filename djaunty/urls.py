from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('bikes/',views.ListBikes.as_view(),name='bikelist'),
    path('renters/', views.ListRenters.as_view(),name='renterlist'),
    path('rentals/', views.ListRentals.as_view(),name='rentallist'),

]
