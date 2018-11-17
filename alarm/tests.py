from django.test import TestCase
from alarm.models import Alarm
from alarm import views
from datetime import datetime


class test(TestCase):
	def setUp(self):
		Alarm.objects.create(
			hour=datetime.now().time(),
			marker='acorda',
			status=True,
			url='dfafafa')

	def testget(self):
		ob = Alarm.objects.get(status=True)
		self.assertEqual(ob.marker,'acorda')

	def delete(self):
		conf = Alarm.objects.get(status=True)
		response = Alarm.objects.delete(conf)
		self.assertEqual(response.status_code , 200)	

	def getall(self): 
		todos = Alarm.objects.all()
		self.assertEqual(todos.status_code , 200)

	def update(self):
		ob = Alarm.objects.get(status=True)
		self.assertEqual(ob.marker , 'acorda')
		ob.marker = 'acorda agora'
		ob.save()
		self.assertEqual(ob.marker , 'acorda agora')



