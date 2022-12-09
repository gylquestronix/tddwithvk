from django.urls import path

from . import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('reservations/', views.getReservations, name='reservations'),
    path('perform/', views.getPerformance, name='perform'),
    path('reservations/<int:id>/', views.getReservation, name='reservation'),
    path('rentals/', views.getRentals, name='rentals'),
    # path('rentals/<int:id>/',views.getRental),
]