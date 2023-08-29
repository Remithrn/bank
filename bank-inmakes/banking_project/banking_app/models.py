from django.db import models

# Create your models here.
from django.db import models

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('cheque', 'Cheque'),
        ('debit', 'Debit Card'),
        ('credit', 'Credit Card'),
    )

    name = models.CharField(max_length=124)
    dob = models.DateField()  # Date of Birth
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cheque')

    def __str__(self):
        return self.name
