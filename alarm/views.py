from django.shortcuts import render
from alarm.models import Alarm
from alarm.forms import AlarmForm

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


