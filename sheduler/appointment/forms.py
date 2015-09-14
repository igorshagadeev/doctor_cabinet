# -*- coding: utf-8 -*-

from django import forms

from appointment.models import Appointment





class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'surname', 'patronymic', 'doctor',]
