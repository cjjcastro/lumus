from django import forms
from alarm.models import Alarm

class AlarmForm(forms.ModelForm):
    
    class Meta:
        model = Alarm
        fields = [  'hour',
                    'marker',
                	'status',
                    'useUrl',
                    'url',
                    'snooze']