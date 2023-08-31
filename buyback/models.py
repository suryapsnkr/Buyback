from django.db import models
from datetime import date
from django.utils.timezone import now

class Companie(models.Model):
    symbol = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    logo = models.FileField(upload_to='static/media/')
    odate = models.DateField(verbose_name=('Open Date'))
    cdate = models.DateField(verbose_name=('Close Date'))
    price = models.CharField(max_length=32)
    size = models.CharField(max_length=32)

    def __str__(self):
        return str(self.symbol)

class Client(models.Model):
    ccode = models.CharField(verbose_name=('Code'), max_length=32)
    cname = models.CharField(verbose_name=('Name'), max_length=32)
    pan = models.CharField(verbose_name=('PAN'), max_length=32)
    dac = models.CharField(verbose_name=('DEMAT A/C'), max_length=32)
    mobile = models.CharField(verbose_name=('Mobile'), max_length=32)
    symbol = models.CharField(max_length=32)
    qty = models.CharField(verbose_name=('Quantity'), max_length=32)
    status = models.BooleanField(verbose_name=('Status'), default=False)
    adate = models.DateField(verbose_name=('Apllied'),auto_now=True)

    def __str__(self):
        return str(self.ccode)

    
