from django.shortcuts import render, redirect
from alarm.models import Alarm
from alarm.forms import AlarmForm
import datetime

# Create your views here.
def home(request):
    return render(request, 'alarm/home.html', {})


def alarm(request):
    alarms = Alarm.objects.all()
    form = AlarmForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'alarm/alarm.html', {'alarms': alarms, 'form': form})


def delete(request, part_id =None):
    object = Alarm.objects.get(id=part_id)
    object.delete()
    return redirect('alarm')


def update(request, part_id = None):
    object = Alarm.objects.get(id=part_id)
    object.status = not(object.status)
    object.save()
    return redirect('alarm')


