from django.db import models

# Create your models here.
class Car(models.Model):
    # pk-primary key
    brand = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"PK{self.pk}: {self.brand} in the year {self.year}."