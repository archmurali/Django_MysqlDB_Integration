from django.test import TestCase
from .models import OcCart


class OcCartTest(TestCase):

	def setUp(self):
		OcCart.objects.create(cart_id=100,customer_id=30,product_id=31)

	def getdata(self);
		a = OcCart.objects.get(cart_id=13)
		self.assertEqual(a,28)