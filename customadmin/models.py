from django.db import models

# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=100)
    county_no = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=254)
    license_no = models.CharField(max_length=20, blank=True, null=True)
    county = models.ForeignKey(County, blank=True, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} -> { self.county }'