from django.urls import path
from .views import (
    VehicleListAPIView,
    VehicleDetailAPIView,
    BookingListAPIView,
    BookingDetailAPIView,
)

urlpatterns = [

    path("vehicles/", VehicleListAPIView.as_view()),
    path("vehicles/<int:id>/", VehicleDetailAPIView.as_view()),

    path("bookings/", BookingListAPIView.as_view()),
    path("bookings/<int:id>/", BookingDetailAPIView.as_view()),
]
