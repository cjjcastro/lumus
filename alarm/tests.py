from django.test import TestCase
from alarm.models import Alarm
from alarm import views
from datetime import datetime
from django.test import Client, RequestFactory
from django.urls import reverse


class test(TestCase):
	def setUp(self):
		Alarm.objects.create(
			hour=datetime.now().time(),
			marker='acorda',
			status=True,
			url='dfafafa') #id=1

	def test_get(self):
		ob = Alarm.objects.get(status=True)
		self.assertEqual(ob.marker,'acorda')

	def test_delete(self):
		conf = Alarm.objects.get(status=True)
		conf.delete()
		self.assertEqual(Alarm.objects.all().count() , 0)	

	def test_get_all(self): 
		todos = Alarm.objects.all()
		self.assertEqual(todos.count(), 1)

	def test_update(self):
		ob = Alarm.objects.get(status=True)
		self.assertEqual(ob.marker , 'acorda')
		ob.marker = 'acorda agora'
		ob.save()
		self.assertEqual(ob.marker , 'acorda agora')

	def test_delete_view(self):
		request = RequestFactory().get('/delete/')
		views.delete(request, 1)
		self.assertEqual(Alarm.objects.all().count() , 0)

	def test_update_view(self):
		request = RequestFactory().get('/update/')
		views.update(request, 1)
		ob = Alarm.objects.get(id=1)
		self.assertEqual(ob.status, False)

class ProjectTests(TestCase):
	def test_homepage(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_alarm_page(self):
		response = self.client.get(reverse('alarm'))
		self.assertEqual(response.status_code, 200)