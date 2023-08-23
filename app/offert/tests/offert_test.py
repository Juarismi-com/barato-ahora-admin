from django.test import TestCase
from ..models import OffertCategory, Offert, Business, OffertType
import datetime
from django.utils.timezone import make_aware
from django.contrib.auth.models import User

class OffertModelTest(TestCase):
   def setUp(self):
      self.user_created = User(email="test@test.com", username="test")
      self.user_created.save()
      
      self.business_create = Business(name="business_a")
      self.business_create.save()

      self.offert_type_created = OffertType(name='discount')
      self.offert_type_created.save()

      self.category_created = OffertCategory(name='category_x')
      self.category_created.save()

      self.offert_created = Offert(
         title="offert_y", 
         category=self.category_created,
         date_start=make_aware(datetime.datetime.now()),
         date_end=make_aware(datetime.datetime.now()),
         disclaimer="nothing",
         business_receptor=self.business_create,
         user_created=self.user_created,
         offert_type=self.offert_type_created,
         discount_rate=10.99
      )
      self.offert_created.save()

   def test_get_offert_by_category(self):
      offert = Offert.objects.filter(category=self.category_created)
      self.assertEqual(offert[0].title, 'offert_y')

   def test_get_offert_is_not_exist_by_category(self):
      offert = Offert.objects.filter(category=self.category_created)
      self.assertIsNot(offert[0].title, 'offert_z')


   def tearDown(self):
      self.offert_created.delete()
      self.category_created.delete()
      self.business_create.delete()
      self.offert_type_created.delete()
      self.user_created.delete()
      