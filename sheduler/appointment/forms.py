# django
from django import forms

# project
from appointment.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'surname', 'patronymic', 'doctor', ]
