from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Q
from .models import Room, Guest, Staff, Reservation, Payment, HousekeepingLog, BookingStatus, RoomStatus
from .forms import (
    RoomForm, GuestForm, StaffForm, ReservationForm, PaymentForm,
    HousekeepingForm, OnlineBookingForm, GuestRegistrationForm,
)


def is_staff_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


# ── Public Website ────────────────────────────────────────────────────
def home(request):
    rooms = Room.objects.filter(status=RoomStatus.AVAILABLE)[:4]
    featured = [
        {'title': 'Alpine View Room', 'image': 'alpine.jpg', 'price': '8,500', 'icons': 5},
        {'title': 'Deluxe Mountain Suite', 'image': 'deluxe.jpg', 'price': '12,000', 'icons': 4},
        {'title': 'Lake View Chalet', 'image': 'chalet.jpg', 'price': '10,500', 'icons': 3},
        {'title': 'Valley Room', 'image': 'standard.jpg', 'price': '6,500', 'icons': 2},
    ]
    facilities = [
        {'name': 'Kutwal Lake Tours', 'image': 'lake.jpg', 'desc': 'Guided walks to the crystal-clear alpine lake'},
        {'name': 'Haramosh Trekking', 'image': 'trekking.jpg', 'desc': 'Expert guides for Haramosh Valley treks'},
        {'name': 'Traditional Restaurant', 'image': 'restaurant.jpg', 'desc': 'Local cuisine with mountain views'},
        {'name': 'Bonfire & BBQ', 'image': 'bonfire.jpg', 'desc': 'Evening bonfire under the Karakoram stars'},
        {'name': 'Jeep Safari', 'image': 'jeep.jpg', 'desc': '4x4 transport from Sassi to Kutwal Valley'},
    ]
    booking_form = OnlineBookingForm()
    return render(request, 'public/home.html', {
        'rooms': rooms,
        'featured': featured,
        'facilities': facilities,
        'booking_form': booking_form,
    })


def public_booking(request):
    if request.method != 'POST':
        return redirect('home')

    form = OnlineBookingForm(request.POST)
    if not form.is_valid():
        messages.error(request, 'Please correct the booking form errors.')
        return redirect('home#booking')

    data = form.cleaned_data
    room = Room.objects.filter(
        room_type=data['room_type'],
        status=RoomStatus.AVAILABLE,
    ).first()
    if not room:
        messages.error(request, 'No room of this type is currently available. Please try another room.')
        return redirect('home#rooms')

    guest, _ = Guest.objects.get_or_create(
        email=data['email'],
        defaults={
            'first_name': data['first_name'],
            'last_name': data.get('last_name') or '',
            'phone': data['phone'],
            'cnic': data['cnic'],
            'country': data['country'],
            'nationality': data['country'],
            'user': request.user if request.user.is_authenticated else None,
        },
    )
    if guest.first_name != data['first_name']:
        guest.first_name = data['first_name']
        guest.last_name = data.get('last_name') or ''
        guest.phone = data['phone']
        guest.save()

    Reservation.objects.create(
        guest=guest,
        room=room,
        check_in=data['check_in'],
        check_out=data['check_out'],
        num_guests=data['num_guests'],
        bed_type=data['bed_type'],
        meal_plan=data['meal_plan'],
        status=BookingStatus.PENDING,
        notes=data.get('notes', ''),
    )
    messages.success(
        request,
        f'Booking request submitted! We will confirm your stay at Kutwal Dream Resort shortly. '
        f'Reference: {guest.full_name} | {room.room_type} | {data["check_in"]} to {data["check_out"]}',
    )
    return redirect('home')


def guest_register(request):
    if request.user.is_authenticated:
        return redirect('my_bookings')
    form = GuestRegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        Guest.objects.create(
            user=user,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            cnic=form.cleaned_data['cnic'],
        )
        login(request, user)
        messages.success(request, 'Welcome to Kutwal Dream Resort! Your account is ready.')
        return redirect('my_bookings')
    return render(request, 'public/register.html', {'form': form})


def guest_login(request):
    if request.user.is_authenticated:
        return redirect('my_bookings')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next', 'my_bookings')
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect(next_url)
        messages.error(request, 'Invalid username or password.')
    return render(request, 'public/login.html')


def guest_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def my_bookings(request):
    guest = Guest.objects.filter(Q(user=request.user) | Q(email=request.user.email)).first()
    reservations = []
    if guest:
        reservations = Reservation.objects.filter(guest=guest).select_related('room').order_by('-created_at')
    return render(request, 'public/my_bookings.html', {'reservations': reservations, 'guest': guest})


def staff_login(request):
    if request.user.is_authenticated and is_staff_user(request.user):
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and is_staff_user(user):
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name or user.username}!')
            return redirect('dashboard')
        messages.error(request, 'Invalid staff credentials.')
    return render(request, 'public/staff_login.html')


# ── Staff Dashboard ───────────────────────────────────────────────────
@user_passes_test(is_staff_user, login_url='staff_login')
def dashboard(request):
    ctx = {
        'total_rooms': Room.objects.count(),
        'available_rooms': Room.objects.filter(status=RoomStatus.AVAILABLE).count(),
        'occupied_rooms': Room.objects.filter(status=RoomStatus.OCCUPIED).count(),
        'total_guests': Guest.objects.count(),
        'total_staff': Staff.objects.count(),
        'active_reservations': Reservation.objects.filter(status=BookingStatus.CHECKED_IN).count(),
        'upcoming': Reservation.objects.filter(status__in=[BookingStatus.PENDING, BookingStatus.CONFIRMED]).count(),
        'total_revenue': Payment.objects.filter(status='Paid').aggregate(t=Sum('amount'))['t'] or 0,
        'pending_payments': Payment.objects.filter(status='Pending').count(),
        'pending_bookings': Reservation.objects.filter(status=BookingStatus.PENDING).count(),
        'recent_reservations': Reservation.objects.select_related('guest', 'room').order_by('-created_at')[:6],
        'rooms': Room.objects.all(),
        'pending_housekeeping': HousekeepingLog.objects.filter(status='Pending').count(),
    }
    return render(request, 'manage/dashboard.html', ctx)


@user_passes_test(is_staff_user, login_url='staff_login')
def room_list(request):
    return render(request, 'manage/room_list.html', {'rooms': Room.objects.all()})


@user_passes_test(is_staff_user, login_url='staff_login')
def room_create(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Room added successfully!')
        return redirect('room_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Add Room', 'back': 'room_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        messages.success(request, 'Room updated!')
        return redirect('room_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Edit Room', 'back': 'room_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted.')
        return redirect('room_list')
    return render(request, 'manage/confirm_delete.html', {'obj': room, 'back': 'room_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def guest_list(request):
    guests = Guest.objects.annotate(res_count=Count('reservations'))
    return render(request, 'manage/guest_list.html', {'guests': guests})


@user_passes_test(is_staff_user, login_url='staff_login')
def guest_create(request):
    form = GuestForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Guest registered!')
        return redirect('guest_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Register Guest', 'back': 'guest_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def guest_edit(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    form = GuestForm(request.POST or None, instance=guest)
    if form.is_valid():
        form.save()
        messages.success(request, 'Guest updated!')
        return redirect('guest_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Edit Guest', 'back': 'guest_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        messages.success(request, 'Guest removed.')
        return redirect('guest_list')
    return render(request, 'manage/confirm_delete.html', {'obj': guest, 'back': 'guest_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def staff_list(request):
    return render(request, 'manage/staff_list.html', {'staff_list': Staff.objects.all()})


@user_passes_test(is_staff_user, login_url='staff_login')
def staff_create(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Staff member added!')
        return redirect('staff_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Add Staff', 'back': 'staff_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    form = StaffForm(request.POST or None, instance=staff)
    if form.is_valid():
        form.save()
        messages.success(request, 'Staff updated!')
        return redirect('staff_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Edit Staff', 'back': 'staff_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        messages.success(request, 'Staff removed.')
        return redirect('staff_list')
    return render(request, 'manage/confirm_delete.html', {'obj': staff, 'back': 'staff_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def reservation_list(request):
    reservations = Reservation.objects.select_related('guest', 'room', 'handled_by').order_by('-created_at')
    return render(request, 'manage/reservation_list.html', {'reservations': reservations})


@user_passes_test(is_staff_user, login_url='staff_login')
def reservation_create(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        res = form.save()
        if res.status in (BookingStatus.CONFIRMED, BookingStatus.CHECKED_IN):
            res.room.status = RoomStatus.OCCUPIED
            res.room.save()
        messages.success(request, 'Reservation created!')
        return redirect('reservation_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'New Reservation', 'back': 'reservation_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def reservation_edit(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    form = ReservationForm(request.POST or None, instance=res)
    if form.is_valid():
        form.save()
        messages.success(request, 'Reservation updated!')
        return redirect('reservation_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Edit Reservation', 'back': 'reservation_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def reservation_delete(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        res.room.status = RoomStatus.AVAILABLE
        res.room.save()
        res.delete()
        messages.success(request, 'Reservation cancelled.')
        return redirect('reservation_list')
    return render(request, 'manage/confirm_delete.html', {'obj': res, 'back': 'reservation_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def confirm_booking(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    res.status = BookingStatus.CONFIRMED
    res.room.status = RoomStatus.OCCUPIED
    res.room.save()
    res.save()
    messages.success(request, f'Booking confirmed for {res.guest.full_name}.')
    return redirect('reservation_list')


@user_passes_test(is_staff_user, login_url='staff_login')
def checkin(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    res.status = BookingStatus.CHECKED_IN
    res.room.status = RoomStatus.OCCUPIED
    res.room.save()
    res.save()
    messages.success(request, f'{res.guest.full_name} checked in to Room {res.room.room_number}.')
    return redirect('reservation_list')


@user_passes_test(is_staff_user, login_url='staff_login')
def checkout(request, pk):
    res = get_object_or_404(Reservation, pk=pk)
    res.status = BookingStatus.CHECKED_OUT
    res.room.status = RoomStatus.AVAILABLE
    res.room.save()
    res.save()
    HousekeepingLog.objects.create(room=res.room, status='Pending', notes='Post checkout cleaning')
    messages.success(request, f'{res.guest.full_name} checked out. Housekeeping task created.')
    return redirect('reservation_list')


@user_passes_test(is_staff_user, login_url='staff_login')
def payment_list(request):
    payments = Payment.objects.select_related('reservation__guest', 'reservation__room').order_by('-payment_date')
    total_paid = Payment.objects.filter(status='Paid').aggregate(t=Sum('amount'))['t'] or 0
    total_pending = Payment.objects.filter(status='Pending').aggregate(t=Sum('amount'))['t'] or 0
    return render(request, 'manage/payment_list.html', {
        'payments': payments,
        'total_paid': total_paid,
        'total_pending': total_pending,
    })


@user_passes_test(is_staff_user, login_url='staff_login')
def payment_create(request, res_pk):
    res = get_object_or_404(Reservation, pk=res_pk)
    form = PaymentForm(request.POST or None, initial={'amount': res.total_cost})
    if form.is_valid():
        payment = form.save(commit=False)
        payment.reservation = res
        payment.save()
        messages.success(request, 'Payment recorded!')
        return redirect('payment_list')
    return render(request, 'manage/form.html', {
        'form': form,
        'title': f'Record Payment – Res #{res.pk}',
        'back': 'reservation_list',
        'extra_info': f'Guest: {res.guest.full_name} | Room: {res.room} | Total Due: PKR {res.total_cost}',
    })


@user_passes_test(is_staff_user, login_url='staff_login')
def payment_edit(request, pk):
    pay = get_object_or_404(Payment, pk=pk)
    form = PaymentForm(request.POST or None, instance=pay)
    if form.is_valid():
        form.save()
        messages.success(request, 'Payment updated!')
        return redirect('payment_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Edit Payment', 'back': 'payment_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def housekeeping_list(request):
    logs = HousekeepingLog.objects.select_related('room', 'staff').order_by('-date')
    return render(request, 'manage/housekeeping_list.html', {'logs': logs})


@user_passes_test(is_staff_user, login_url='staff_login')
def housekeeping_create(request):
    form = HousekeepingForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Housekeeping task added!')
        return redirect('housekeeping_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Add Housekeeping Task', 'back': 'housekeeping_list'})


@user_passes_test(is_staff_user, login_url='staff_login')
def housekeeping_edit(request, pk):
    log = get_object_or_404(HousekeepingLog, pk=pk)
    form = HousekeepingForm(request.POST or None, instance=log)
    if form.is_valid():
        form.save()
        messages.success(request, 'Task updated!')
        return redirect('housekeeping_list')
    return render(request, 'manage/form.html', {'form': form, 'title': 'Update Task', 'back': 'housekeeping_list'})
