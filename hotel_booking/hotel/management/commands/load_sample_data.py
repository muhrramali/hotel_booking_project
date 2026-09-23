from datetime import date, timedelta
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from hotel.models import Room, Guest, Staff, Reservation, Payment, HousekeepingLog, BookingStatus


class Command(BaseCommand):
    help = 'Load sample data for Kutwal Dream Resort'

    def handle(self, *args, **options):
        if Room.objects.exists():
            self.stdout.write('Sample data already exists. Skipping.')
            return

        rooms = [
            ('101', 'Alpine View', 2, 8500, 2, 'Double', 'alpine.jpg', 'Panoramic view of Haramosh peaks'),
            ('102', 'Alpine View', 2, 8500, 2, 'Double', 'alpine.jpg', 'Mountain-facing balcony'),
            ('201', 'Deluxe Suite', 2, 12000, 3, 'Double', 'deluxe.jpg', 'Luxury suite with sitting area'),
            ('202', 'Deluxe Suite', 2, 12000, 4, 'Quad', 'deluxe.jpg', 'Family deluxe with fireplace'),
            ('301', 'Lake Chalet', 3, 10500, 2, 'Double', 'chalet.jpg', 'Steps away from Kutwal Lake trail'),
            ('302', 'Lake Chalet', 3, 10500, 3, 'Triple', 'chalet.jpg', 'Lake view chalet with heater'),
            ('401', 'Valley Room', 1, 6500, 2, 'Double', 'standard.jpg', 'Cozy valley-facing room'),
            ('402', 'Valley Room', 1, 6500, 2, 'Double', 'standard.jpg', 'Budget-friendly mountain room'),
            ('501', 'Guest Cabin', 1, 7500, 4, 'Quad', 'chalet.jpg', 'Wooden cabin for groups'),
            ('601', 'Trekker Room', 1, 4500, 1, 'Single', 'standard.jpg', 'Basic room for solo trekkers'),
        ]
        for num, rtype, floor, price, cap, bed, img, desc in rooms:
            Room.objects.create(
                room_number=num, room_type=rtype, floor=floor,
                price_per_night=Decimal(price), capacity=cap, bed_type=bed,
                image=img, description=desc, status='Available',
            )

        staff_user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@kutwaldreamresort.com', 'first_name': 'Resort', 'last_name': 'Admin', 'is_staff': True, 'is_superuser': True},
        )
        if created:
            staff_user.set_password('admin123')
            staff_user.save()

        staff_members = [
            ('Ahmed Khan', 'Manager', '+92 300 1111111', 'ahmed@kutwal.com', 'Morning', 85000),
            ('Sara Ali', 'Receptionist', '+92 300 2222222', 'sara@kutwal.com', 'Morning', 45000),
            ('Hassan Raza', 'Trek Guide', '+92 300 3333333', 'hassan@kutwal.com', 'Morning', 55000),
            ('Fatima Noor', 'Housekeeping', '+92 300 4444444', 'fatima@kutwal.com', 'Morning', 35000),
            ('Imran Shah', 'Chef', '+92 300 5555555', 'imran@kutwal.com', 'Evening', 50000),
        ]
        today = date.today()
        staff_objs = []
        for name, role, phone, email, shift, salary in staff_members:
            staff_objs.append(Staff.objects.create(
                name=name, role=role, phone=phone, email=email,
                shift=shift, salary=Decimal(salary), hired_date=today - timedelta(days=180),
            ))

        guests_data = [
            ('Ali', 'Hassan', 'ali@email.com', '+92 321 0000001', '35201-1234567-1'),
            ('Zainab', 'Malik', 'zainab@email.com', '+92 322 0000002', '35201-2345678-2'),
            ('Usman', 'Tariq', 'usman@email.com', '+92 323 0000003', '35201-3456789-3'),
        ]
        guest_objs = []
        for fn, ln, email, phone, cnic in guests_data:
            guest_objs.append(Guest.objects.create(
                first_name=fn, last_name=ln, email=email, phone=phone, cnic=cnic,
                nationality='Pakistani', country='Pakistan',
            ))

        res1 = Reservation.objects.create(
            guest=guest_objs[0], room=Room.objects.get(room_number='101'),
            handled_by=staff_objs[1], check_in=today + timedelta(days=2),
            check_out=today + timedelta(days=5), num_guests=2,
            meal_plan='Breakfast', status=BookingStatus.CONFIRMED,
        )
        res1.room.status = 'Occupied'
        res1.room.save()

        res2 = Reservation.objects.create(
            guest=guest_objs[1], room=Room.objects.get(room_number='301'),
            handled_by=staff_objs[1], check_in=today - timedelta(days=1),
            check_out=today + timedelta(days=2), num_guests=2,
            meal_plan='Half Board', status=BookingStatus.CHECKED_IN,
        )
        res2.room.status = 'Occupied'
        res2.room.save()

        Payment.objects.create(reservation=res2, amount=res2.total_cost, method='Cash', status='Paid')

        Reservation.objects.create(
            guest=guest_objs[2], room=Room.objects.get(room_number='601'),
            check_in=today + timedelta(days=7), check_out=today + timedelta(days=10),
            num_guests=1, meal_plan='Room only', status=BookingStatus.PENDING,
        )

        HousekeepingLog.objects.create(room=Room.objects.get(room_number='402'), staff=staff_objs[3], status='Pending', notes='Daily cleaning')

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))
        self.stdout.write('Staff login: admin / admin123')
