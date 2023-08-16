from django.test import TestCase
from .models import OffertCategory
# Create your tests here.
class OffertCategoryModelTest(TestCase):
   def setUp(self):
      self.category_created = OffertCategory(name='test_1')
      self.category_created.save()

   def test_get_by_name(self):
      self.assertEqual(self.category_created.name, 'test_1')

   def test_failed_by_name(self):
      self.assertIsNot(self.category_created.name, 'test_2')

   def tearDown(self):
        self.category_created.delete()
