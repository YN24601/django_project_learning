from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(0), MaxValueValidator(200)])

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'