from django.db import models

# Create your models here.
class OffertType(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name


class Business(models.Model):
   name = models.CharField(max_length=200)
   logo = models.TextField()

   def __str__(self):
      return self.name


class Offert(models.Model):
   offert_type = models.ForeignKey(OffertType, on_delete=models.CASCADE)
   business_emissor = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_emissor')
   business_receptor = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_receptor')
   date_start = models.DateTimeField("date published")
   date_end = models.DateTimeField()
   title = models.CharField(max_length=200)
   disclaimer = models.CharField(max_length=200, default=None)
   active = models.BooleanField(default=True)
   description = models.TextField()

   def __str__(self):
      return self.title


class OffertDays(models.Model):
   offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
   sunday = models.BooleanField(default=False)
   monday= models.BooleanField(default=False)
   tuesday= models.BooleanField(default=False)
   wednesday= models.BooleanField(default=False)
   thursday= models.BooleanField(default=False)
   friday= models.BooleanField(default=False)
   saturday= models.BooleanField(default=False)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50) 

   