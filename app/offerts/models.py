from django.db import models

# Create your models here.
class OffertType(models.Model):
    name = models.CharField(max_length=200)

class Business(models.Model):
    name = models.CharField(max_length=200)
    logo = models.TextField()


class Offert(models.Model):
    offert_type = models.ForeignKey(OffertType)
    business_emissor_id = models.ForeignKey(Business, default=None)
    business_receptor_id = models.ForeignKey(Business, default=None)
    date_start = models.DateTimeField("date published")
    date_end = models.DateTimeField()
    title = models.CharField(max_length=200)
    disclaimer = models.CharField(max_length=200, default=None)
    active = models.BooleanField(default=True)
    description = models.TextField()


class OffertDays(models.Model):
   offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
   sunday = models.BooleanField(default=False)
   monday= models.BooleanField(default=False)
   tuesday= models.BooleanField(default=False)
   wednesday= models.BooleanField(default=False)
   thursday= models.BooleanField(default=False)
   friday= models.BooleanField(default=False)
   saturday= models.BooleanField(default=False)
