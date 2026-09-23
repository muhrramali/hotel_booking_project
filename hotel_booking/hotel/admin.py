from django.contrib import admin
from .models import Room, Guest, Staff, Reservation, Payment, HousekeepingLog


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'room_type', 'price_per_night', 'capacity', 'status']
    list_filter = ['status', 'room_type']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'cnic', 'country', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'phone', 'email', 'shift']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'guest', 'room', 'check_in', 'check_out', 'status', 'meal_plan']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'amount', 'method', 'status', 'payment_date']


@admin.register(HousekeepingLog)
class HousekeepingLogAdmin(admin.ModelAdmin):
    list_display = ['room', 'staff', 'date', 'status']
