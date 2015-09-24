# django
from django.core.context_processors import csrf
# from django import http
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db import IntegrityError

# models
from doctor.models import Doctor
from appointment.models import Appointment

# forms
from appointment.forms import AppointmentForm

# project
from tools.jsonans import jsonSimpleAns

# python 3.4
from datetime import datetime, timedelta
import json



def main(request):
    """ """
    # today
    today = datetime.today()

    # current week
    # today.isocalendar()[1]

    # monday - friday
    # week_days = [today + timedelta(days=i) for i in range(0 - today.weekday(), 5 - today.weekday())]

    doctors = Doctor.objects.all()

    context = {
        'today': today,
        'doctors': doctors,
    }
    variables = RequestContext(request, context)
    variables.update(csrf(request))
    return render_to_response('main.html', variables)





def get_doctor_shedule(request):
    """
    send json with busy sheduler for doctor
    events = [
    {
        title: 'busy',
        start: '2015-09-16T14:00',
        end: '2015-09-16T15:00',
        color: 'yellow',
    },
    {
        title: 'busy',
        start: '2015-09-17T11:00',
        end: '2015-09-17T12:00',
        color: 'yellow',
    }]
    """
    if request.method != 'GET':
        raise http.Http404

    doctor_id = request.GET.get('doctor_id')
    if doctor_id:
        doctor = Doctor.objects.get(id=doctor_id)

        # today
        today = datetime.today()
        # first monday of this week
        this_week_moday = today + timedelta(days=0 - today.weekday())

        # date grater than today week monday
        appointments = Appointment.objects.filter(doctor=doctor, datetime__gt=this_week_moday)

        dt = timedelta(hours=1)

        events = []
        for a in appointments:
            end = a.datetime + dt
            event = {
                'id': a.datetime.strftime("%Y-%m-%dT%H:%M"),
                'title': 'busy',
                'start': a.datetime.strftime("%Y-%m-%dT%H:%M"),
                'end': end.strftime("%Y-%m-%dT%H:%M"),
                'color': 'yellow',
            }
            events.append(event)

        events_json = json.dumps(events)
    else:
        return jsonSimpleAns(error='error')

    return jsonSimpleAns(info={'events_json': events_json})





def save_appointment(request):
    """
    """
    if request.method != 'POST':
        raise http.Http404

    appointment_form = AppointmentForm(request.POST)

    if appointment_form.is_valid():
        try:
            appointment = appointment_form.save(commit=False)
            form_dt = request.POST.get('datetime')
            # Tue Sep 15 2015 11:00:00 GMT+0000
            dt_obj = datetime.strptime(form_dt, "%a %b %d %Y %H:%M:%S GMT+0000")
            appointment.datetime = dt_obj
            appointment.save()

        except IntegrityError:
            return jsonSimpleAns(error='error')

    else:
        return jsonSimpleAns(error=appointment_form.errors)

    return render_to_response('success.html')


























