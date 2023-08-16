from django.test import TestCase
from ..models import OffertCategory, Offert, Business, OffertType
import datetime


class OffertModelTest(TestCase):
   def setUp(self):
      self.business_create = Business(name="business_a")
      self.business_create.save()

      self.offert_type_created = OffertType(name='discount')
      self.offert_type_created.save()

      self.category_created = OffertCategory(name='category_x')
      self.category_created.save()

      self.offert_created = Offert(
         title="offert_y", 
         category=self.category_created,
         date_start=datetime.datetime.now(),
         date_end=datetime.datetime.now(),
         disclaimer="nothing",
         business_receptor=self.business_create,
         business_emissor=self.business_create,
         offert_type=self.offert_type_created,
         discount_rate=10.99
      )
      self.offert_created.save()

   def test_get_offert_by_category(self):
      offert = Offert.objects.filter(category=self.category_created)
      self.assertEqual(offert[0].title, 'offert_y')


   def tearDown(self):
      self.offert_created.delete()
      self.category_created.delete()
      