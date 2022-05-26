import uuid
from django.db import models
from accounts.models import Parent, Doctor
from django.urls import reverse

# Create your models here.

COUNTY_CHOICES = (
    ('NAIROBI COUNTY', 'NAIROBI COUNTY'),
    ('KISUMU COUNTY', 'KISUMU COUNTY'),
    ('NYANDARUA COUNTY', 'NYANDARUA COUNTY'),
    ('NAKURU COUNTY', 'NAKURU COUNTY'),
    ('KERICHO COUNTY', 'KERICHO COUNTY'),
    ('BARINGO COUNTY', 'BARINGO COUNTY'),
    ('LAIKIPIA COUNTY', 'LAIKIPIA COUNTY'),
    ('MAKUENI COUNTY', 'MAKUENI COUNTY'),
    ('BOMET COUNTY', 'BOMET COUNTY'),
    ('BUSIA COUNTY', 'BUSIA COUNTY'),
    ('EMBU COUNTY', 'EMBU COUNTY'),
    ('ISIOLO COUNTY', 'ISIOLO COUNTY'),
    ('NANDI COUNTY', 'NANDI COUNTY'),
    ('NAROK COUNTY', 'NAROK COUNTY'),
    ('NYERI COUNTY', 'NYERI COUNTY'),
    ('KAKAMEGA COUNTY', 'KAKAMEGA COUNTY'),
    ('KERICHO COUNTY', 'KERICHO COUNTY'),
    ('BARINGO COUNTY', 'BARINGO COUNTY'),
)

#vaccines given to kids
VACCINE_CHOICES = (
    (1, 'BCG'),
    (2, 'OPV'),
    (3, 'DPT'),
    (4, 'HEPATITIS B'),
    (5, 'HEPATITIS A'),
    (6, 'MEASLES')
)



class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    birth_no = models.CharField(max_length=50)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mothers_name = models.CharField(max_length=254, blank=True, null=True)
    fathers_name = models.CharField(max_length=254, blank=True, null=True)
    date_of_registration = models.DateTimeField()
    date_of_birth = models.DateTimeField()
    birth_county = models.CharField(max_length=254, choices=COUNTY_CHOICES)
    resident_county = models.CharField(choices=COUNTY_CHOICES, max_length=50, blank=True, null=True)
    height = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    weight = models.PositiveSmallIntegerField(default=0, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('core:child-profile', kwargs={'uuid': self.uuid})


    
    class Meta:
        verbose_name_plural = 'Children'
        db_table = 'child'



class Vaccines(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=254, blank=True, null=True)
    time_given = models.CharField(max_length=254, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vaccine'
        verbose_name_plural = 'Vaccines'
        db_table = 'vaccines'


class ChildImmunization(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(default=0, blank=True)
    height = models.PositiveSmallIntegerField(default=0, blank=True)
    comment = models.TextField(max_length=254, blank=True, null=True)
    date_given = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    is_vaccinated = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.child.first_name} {self.child.last_name} {self.vaccine.name}"

    class Meta:
        verbose_name = 'Child Immunization'
        verbose_name_plural = 'Child Immunizations'
        db_table = 'child_immunization'


    