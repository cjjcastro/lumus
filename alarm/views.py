from django.shortcuts import render
from alarm.models import Alarm
from django.http import HttpResponse
from alarm.forms import AlarmForm
import datetime
from django.utils.timezone import utc

# Create your views here.
def home(request):
    return render(request, 'alarm/home.html', {})

def alarm(request):
    alarms = Alarm.objects.all()
    form = AlarmForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'alarm/alarm.html', {'alarms': alarms, 'form': form})

def nox(request):
    return render(request, 'alarm/nox.html', {})


def home(request):
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	now = datetime.datetime.now().strftime('%H:%M:%S')
	return render(request, 'alarm/alarm.html', {})


