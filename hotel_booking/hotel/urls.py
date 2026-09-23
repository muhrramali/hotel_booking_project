from django.urls import path
from . import views

urlpatterns = [
    # Public website
    path('', views.home, name='home'),
    path('book/', views.public_booking, name='public_booking'),
    path('register/', views.guest_register, name='guest_register'),
    path('login/', views.guest_login, name='guest_login'),
    path('logout/', views.guest_logout, name='guest_logout'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('staff-login/', views.staff_login, name='staff_login'),

    # Staff management
    path('manage/', views.dashboard, name='dashboard'),
    path('manage/rooms/', views.room_list, name='room_list'),
    path('manage/rooms/add/', views.room_create, name='room_create'),
    path('manage/rooms/<int:pk>/edit/', views.room_edit, name='room_edit'),
    path('manage/rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),

    path('manage/guests/', views.guest_list, name='guest_list'),
    path('manage/guests/add/', views.guest_create, name='guest_create'),
    path('manage/guests/<int:pk>/edit/', views.guest_edit, name='guest_edit'),
    path('manage/guests/<int:pk>/delete/', views.guest_delete, name='guest_delete'),

    path('manage/staff/', views.staff_list, name='staff_list'),
    path('manage/staff/add/', views.staff_create, name='staff_create'),
    path('manage/staff/<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('manage/staff/<int:pk>/delete/', views.staff_delete, name='staff_delete'),

    path('manage/reservations/', views.reservation_list, name='reservation_list'),
    path('manage/reservations/new/', views.reservation_create, name='reservation_create'),
    path('manage/reservations/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
    path('manage/reservations/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    path('manage/reservations/<int:pk>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('manage/reservations/<int:pk>/checkin/', views.checkin, name='checkin'),
    path('manage/reservations/<int:pk>/checkout/', views.checkout, name='checkout'),

    path('manage/payments/', views.payment_list, name='payment_list'),
    path('manage/payments/new/<int:res_pk>/', views.payment_create, name='payment_create'),
    path('manage/payments/<int:pk>/edit/', views.payment_edit, name='payment_edit'),

    path('manage/housekeeping/', views.housekeeping_list, name='housekeeping_list'),
    path('manage/housekeeping/add/', views.housekeeping_create, name='housekeeping_create'),
    path('manage/housekeeping/<int:pk>/edit/', views.housekeeping_edit, name='housekeeping_edit'),
]
