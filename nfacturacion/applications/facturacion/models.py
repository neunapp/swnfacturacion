from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Provider(models.Model):

    ruc = models.CharField(
        max_length=11,
        unique=True,
        blank = True
    )
    razon_social = models.CharField(
        max_length=100,
        blank =True
    )
    address = models.CharField(
        max_length=100,
        blank=True
    )

    def __unicode__(self):
        return (self.ruc+'-'+self.razon_social)

class Invoice(models.Model):

    serie = models.CharField(
        max_length=5
    )
    numero = models.CharField(
        max_length=100
    )
    provider = models.ForeignKey(Provider)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    igv = models.DecimalField(max_digits=10, decimal_places=3)
    anulate = models.BooleanField(default=False)

    def __unicode__(self):
        return (self.serie+'-'+self.numero)


class Invoice_Detail(models.Model):

    invoice = models.ForeignKey(Invoice)
    #service = models.ForeignKey(Service)
    service = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return (self.service)
