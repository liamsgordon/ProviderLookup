from django.db import models

# Create your models here.
class provider(models.Model):
    id = models.CharField(primary_key=True, max_length = 20, default='')
    npi = models.CharField(max_length = 10, default='')
    entity = models.CharField("Entity code", max_length = 10, default='')
    first_name = models.CharField("First Name", max_length=50, default='')
    last_name = models.CharField("Last Name", max_length=50, default='')
    organization = models.CharField(max_length=255, default='')
    postal_code = models.CharField("Postal Code", max_length = 50, default='')
    city = models.CharField(max_length = 50, blank = False, default='')
    state = models.CharField("State", max_length = 40, default='')
    address = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    telephone_number = models.CharField(max_length = 50, default='')
    mail_postal_code = models.CharField(max_length = 50, default='')
    mail_city = models.CharField(max_length = 50, blank = False, default='')
    mail_state = models.CharField(max_length = 40, default='')
    mail_address = models.CharField(max_length=255, default='')
    mail_country= models.CharField(max_length=255, default='')
    gender = models.CharField(max_length = 255, default='')
    sole_proprietor = models.CharField(max_length=255, default='')
    enumeration_date = models.CharField(max_length=255, default='')
    certification_date = models.CharField(max_length=255, default='')
    tax_code = models.CharField(max_length=255, default='')
    tax_group = models.CharField(max_length=255, default='')
    tax_defintion = models.CharField(max_length=5000, default='')
    tax_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.npi
