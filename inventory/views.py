from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer

        
class VehicleListAPIView(APIView):

    def get(self, request):

        vehicles = Vehicle.objects.all()

        # Filtering support
        brand = request.GET.get("brand")
        fuel_type = request.GET.get("fuel_type")
        is_available = request.GET.get("is_available")

        if brand:
            vehicles = vehicles.filter(brand=brand)

        if fuel_type:
            vehicles = vehicles.filter(fuel_type=fuel_type)

        if is_available:
            vehicles = vehicles.filter(
                is_available=is_available.lower() == "true"
            )

        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = VehicleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetailAPIView(APIView):

    def get(self, request, id):

        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            return Response({"error": "Vehicle not found"}, status=404)

        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, id):

        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            return Response({"error": "Vehicle not found"}, status=404)

        serializer = VehicleSerializer(vehicle, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, id):

        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            return Response({"error": "Vehicle not found"}, status=404)

        vehicle.delete()
        return Response({"message": "Vehicle deleted successfully"})

class BookingListAPIView(APIView):

    def get(self, request):

        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class BookingDetailAPIView(APIView):

    def get(self, request, id):

        try:
            booking = Booking.objects.get(id=id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=404)

        serializer = BookingSerializer(booking)
        return Response(serializer.data)
