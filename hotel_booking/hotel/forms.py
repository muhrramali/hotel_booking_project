from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room, Guest, Staff, Reservation, Payment, HousekeepingLog, BedType, MealPlan


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_number', 'room_type', 'floor', 'price_per_night', 'capacity',
            'bed_type', 'status', 'has_wifi', 'has_heater', 'has_view', 'image', 'description',
        ]
        widgets = {'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})}


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = [
            'first_name', 'last_name', 'gender', 'email', 'phone',
            'cnic', 'nationality', 'country', 'address',
        ]
        widgets = {'address': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'})}


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'role', 'phone', 'email', 'shift', 'salary', 'hired_date']
        widgets = {'hired_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})}


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'guest', 'room', 'handled_by', 'check_in', 'check_out',
            'num_guests', 'bed_type', 'meal_plan', 'status', 'notes',
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

    def clean(self):
        cleaned = super().clean()
        check_in = cleaned.get('check_in')
        check_out = cleaned.get('check_out')
        if check_in and check_out and check_out <= check_in:
            raise forms.ValidationError('Check-out must be after check-in.')
        return cleaned


class OnlineBookingForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name (optional)'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    country = forms.CharField(max_length=50, initial='Pakistan', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnic = forms.CharField(max_length=20, label='CNIC / Passport', widget=forms.TextInput(attrs={'class': 'form-control'}))
    room_type = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-select'}))
    bed_type = forms.ChoiceField(choices=BedType.choices, widget=forms.Select(attrs={'class': 'form-select'}))
    meal_plan = forms.ChoiceField(choices=MealPlan.choices, widget=forms.Select(attrs={'class': 'form-select'}))
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    num_guests = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Special requests...'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        room_types = Room.objects.filter(status='Available').values_list('room_type', flat=True).distinct()
        self.fields['room_type'].choices = [('', 'Select Room Type')] + [(rt, rt) for rt in room_types]

    def clean(self):
        cleaned = super().clean()
        check_in = cleaned.get('check_in')
        check_out = cleaned.get('check_out')
        if check_in and check_out and check_out <= check_in:
            raise forms.ValidationError('Check-out must be after check-in.')
        return cleaned


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'method', 'status', 'transaction_id', 'remarks']


class HousekeepingForm(forms.ModelForm):
    class Meta:
        model = HousekeepingLog
        fields = ['room', 'staff', 'status', 'notes']


class GuestRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnic = forms.CharField(max_length=20, label='CNIC / Passport', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('username', 'password1', 'password2'):
            self.fields[name].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if Guest.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
