from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    office = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    start_date = models.DateField()
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class AccountEntry(models.Model):
    DATA = models.DateField()
    CONTO = models.CharField(max_length=50)
    ENTRATE = models.FloatField()
    STIPENDIO = models.FloatField()
    USCITE = models.FloatField()
    SALDO = models.FloatField()
    VALUTA = models.IntegerField()

    def __str__(self):
        return self.name