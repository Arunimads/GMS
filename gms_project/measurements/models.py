from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Measurements(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    height=models.DecimalField(max_digits=5,decimal_places=2)
    weight=models.DecimalField(max_digits=5,decimal_places=2)
    biceps=models.DecimalField(max_digits=5,decimal_places=2)
    forearm=models.DecimalField(max_digits=5,decimal_places=2)
    shoulder=models.DecimalField(max_digits=5,decimal_places=2)
    chest=models.DecimalField(max_digits=5,decimal_places=2)
    waist=models.DecimalField(max_digits=5,decimal_places=2)
    thighs=models.DecimalField(max_digits=5,decimal_places=2)
    calf=models.DecimalField(max_digits=5,decimal_places=2)
    measured_date=models.DateField(null=True)

class Meta:
    db_table='Measurements'
