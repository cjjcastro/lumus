from django.test import TestCase
from alarm.models import Alarm
from alarm import views
from datetime import datetime


class test(TestCase):
	def setUp(self):
		Alarm.objects.create(hour=datetime.now().time(),marker='acorda',status='on',url='dfafafa')

	def testget(self):
		ob = Alarm.objects.get(status='on')
		self.assertEqual(ob.marker,'acorda')

	def delete(self):
		conf = Alarm.objects.get(status='on')
		response = Alarm.objects.delete(conf)
		self.assertEqual(response.status_code , 200)	

	def getall(self): 
		todos = Alarm.objects.all()
		self.assertEqual(todos.status_code , 200)	 


			
# Create your tests here.


