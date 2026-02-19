from rest_framework import serializers
from datetime import date

from .models import Vehicle, Booking


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

    #Phone validation
    def validate_customer_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError("Phone must contain only digits.")

        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")

        return value

    #Booking  validation
    def validate(self, data):

        vehicle = data["vehicle"]
        start_date = data["start_date"]
        end_date = data["end_date"]

        
        if start_date < date.today():
            raise serializers.ValidationError("Start date cannot be in the past.")

        
        if end_date <= start_date:
            raise serializers.ValidationError("End date must be after start date.")

        # Overlap booking check
        overlapping = Booking.objects.filter(
            vehicle=vehicle,
            start_date__lte=end_date,
            end_date__gte=start_date
        )

        if overlapping.exists():
            raise serializers.ValidationError(
                "This vehicle is already booked for these dates."
            )

        return data

    #Auto total calculation + vehicle unavailability
    def create(self, validated_data):

        vehicle = validated_data["vehicle"]
        start_date = validated_data["start_date"]
        end_date = validated_data["end_date"]

        days = (end_date - start_date).days
        total_amount = days * vehicle.price_per_day

        booking = Booking.objects.create(
            **validated_data,
            total_amount=total_amount
        )

        vehicle.is_available = False
        vehicle.save()

        return booking
