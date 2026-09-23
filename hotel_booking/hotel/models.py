from django.db import models
from django.contrib.auth.models import User


class RoomType(models.TextChoices):
    ALPINE_VIEW   = 'Alpine View',   'Alpine View Room'
    DELUXE_SUITE  = 'Deluxe Suite',  'Deluxe Mountain Suite'
    LAKE_CHALET   = 'Lake Chalet',   'Kutwal Lake View Chalet'
    VALLEY_ROOM   = 'Valley Room',   'Standard Valley Room'
    GUEST_CABIN   = 'Guest Cabin',   'Guest House Cabin'
    TREKKER_ROOM  = 'Trekker Room',  'Single Trekker Room'


class RoomStatus(models.TextChoices):
    AVAILABLE   = 'Available',   'Available'
    OCCUPIED    = 'Occupied',    'Occupied'
    MAINTENANCE = 'Maintenance', 'Maintenance'


class BedType(models.TextChoices):
    SINGLE = 'Single', 'Single'
    DOUBLE = 'Double', 'Double'
    TRIPLE = 'Triple', 'Triple'
    QUAD   = 'Quad',   'Quad'


class MealPlan(models.TextChoices):
    ROOM_ONLY  = 'Room only',  'Room Only'
    BREAKFAST  = 'Breakfast',  'Breakfast'
    HALF_BOARD = 'Half Board', 'Half Board'
    FULL_BOARD = 'Full Board', 'Full Board'


class BookingStatus(models.TextChoices):
    PENDING   = 'Pending',   'Pending Confirmation'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CHECKED_IN  = 'Checked In',  'Checked In'
    CHECKED_OUT = 'Checked Out', 'Checked Out'
    CANCELLED = 'Cancelled', 'Cancelled'


class PaymentStatus(models.TextChoices):
    PENDING  = 'Pending',  'Pending'
    PAID     = 'Paid',     'Paid'
    REFUNDED = 'Refunded', 'Refunded'


class Room(models.Model):
    room_number     = models.CharField(max_length=10, unique=True)
    room_type       = models.CharField(max_length=30, choices=RoomType.choices, default=RoomType.VALLEY_ROOM)
    floor           = models.PositiveIntegerField(default=1)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity        = models.PositiveIntegerField(default=2)
    bed_type        = models.CharField(max_length=10, choices=BedType.choices, default=BedType.DOUBLE)
    status          = models.CharField(max_length=20, choices=RoomStatus.choices, default=RoomStatus.AVAILABLE)
    has_wifi        = models.BooleanField(default=True)
    has_heater      = models.BooleanField(default=True)
    has_view        = models.BooleanField(default=True, verbose_name='Mountain/Lake View')
    image           = models.CharField(max_length=100, blank=True, help_text='Static image path under static/images/rooms/')
    description     = models.TextField(blank=True)

    class Meta:
        ordering = ['room_number']

    def __str__(self):
        return f"Room {self.room_number} – {self.room_type}"

    @property
    def image_url(self):
        if self.image:
            return f'/static/images/rooms/{self.image}'
        mapping = {
            'Alpine View': 'alpine.jpg',
            'Deluxe Suite': 'deluxe.jpg',
            'Lake Chalet': 'chalet.jpg',
            'Valley Room': 'standard.jpg',
            'Guest Cabin': 'chalet.jpg',
            'Trekker Room': 'standard.jpg',
        }
        return f'/static/images/rooms/{mapping.get(self.room_type, "standard.jpg")}'


class Guest(models.Model):
    GENDER = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]

    user        = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='guest_profile')
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    gender      = models.CharField(max_length=10, choices=GENDER, default='Male')
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=20)
    cnic        = models.CharField(max_length=20, verbose_name='CNIC / Passport')
    nationality = models.CharField(max_length=50, default='Pakistani')
    country     = models.CharField(max_length=50, default='Pakistan')
    address     = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Staff(models.Model):
    ROLES = [
        ('Manager', 'Manager'),
        ('Receptionist', 'Receptionist'),
        ('Housekeeping', 'Housekeeping'),
        ('Guide', 'Trek Guide'),
        ('Chef', 'Chef'),
    ]
    SHIFTS = [('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')]

    user       = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_profile')
    name       = models.CharField(max_length=100)
    role       = models.CharField(max_length=30, choices=ROLES)
    phone      = models.CharField(max_length=20)
    email      = models.EmailField(unique=True)
    shift      = models.CharField(max_length=20, choices=SHIFTS, default='Morning')
    salary     = models.DecimalField(max_digits=10, decimal_places=2)
    hired_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.role})"


class Reservation(models.Model):
    guest       = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    room        = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    handled_by  = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservations')
    check_in    = models.DateField()
    check_out   = models.DateField()
    num_guests  = models.PositiveIntegerField(default=1)
    bed_type    = models.CharField(max_length=10, choices=BedType.choices, default=BedType.DOUBLE)
    meal_plan   = models.CharField(max_length=20, choices=MealPlan.choices, default=MealPlan.ROOM_ONLY)
    status      = models.CharField(max_length=20, choices=BookingStatus.choices, default=BookingStatus.PENDING)
    notes       = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Res#{self.pk} – {self.guest} | {self.room}"

    @property
    def nights(self):
        return max((self.check_out - self.check_in).days, 1)

    @property
    def total_cost(self):
        return self.nights * self.room.price_per_night

    @property
    def status_label(self):
        return self.get_status_display()

    @property
    def is_checked_in(self):
        return self.status == BookingStatus.CHECKED_IN

    @property
    def is_checked_out(self):
        return self.status == BookingStatus.CHECKED_OUT


class Payment(models.Model):
    METHODS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    reservation    = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='payment')
    amount         = models.DecimalField(max_digits=10, decimal_places=2)
    method         = models.CharField(max_length=30, choices=METHODS, default='Cash')
    status         = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    transaction_id = models.CharField(max_length=60, blank=True)
    payment_date   = models.DateField(auto_now_add=True)
    remarks        = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-payment_date']

    def __str__(self):
        return f"Pay#{self.pk} – Res#{self.reservation_id} – {self.status}"


class HousekeepingLog(models.Model):
    STATUS = [('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Done', 'Done')]

    room   = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaning_logs')
    staff  = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    date   = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    notes  = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Cleaning {self.room} on {self.date} – {self.status}"
