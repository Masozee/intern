from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Users(models.Model):
    nama = models.CharField(max_length=150)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Nomor Hp menggunakan format: '+999999999'. maksimal nomor hp yaitu 15 karakter.")
    nomor_hp = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    pekerjaan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama