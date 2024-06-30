from django.db import models
from django.contrib.auth.models import User

class  MemberRegisters(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    join_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table='member_registers'

class TrainerRegisters(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    hire_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table='trainer_registers'

