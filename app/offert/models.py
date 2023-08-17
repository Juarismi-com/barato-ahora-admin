from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserCompany(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    contrasena = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    categoria = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        # Antes de guardar, asegúrate de que la contraseña esté hasheada
        if not self.contrasena.startswith('bcrypt_sha256$'):
            self.contrasena = make_password(self.contrasena)
        super(UserCompany, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class OffertType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
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
    business_emissor = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='business_emissor')
    business_receptor = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='business_receptor')
    date_start = models.DateTimeField("date published")
    date_end = models.DateTimeField()
    title = models.CharField(max_length=200)
    disclaimer = models.CharField(max_length=200, default=None)
    active = models.BooleanField(default=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class OffertDays(models.Model):
    offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
