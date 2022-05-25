from tabnanny import verbose
import uuid
from django.db import models
from accounts.models import Parent, Doctor

# Create your models here.

COUNTY_CHOICES = (
    (1, 'NAIROBI COUNTY'),
    (2, 'KISUMU COUNTY'),
    (3, 'NYANDARUA COUNTY'),
    (4, 'NAKURU COUNTY'),
    (5, 'KERICHO COUNTY'),
    (6, 'MAKUENI COUNTY'),
    (7, 'LAIKIPIA COUNTY'),
    (8, 'BUSIA COUNTY'),
    (9, 'TANA RIVER COUNTY'),
    (10, 'WEST POKOT COUNTY'),
    (11, 'BARINGO COUNTY'),
    (12, 'BOMET COUNTY'),
    (13, 'BUNGOMA COUNTY'),
    (14, 'BUSIA COUNTY'),
    (15, 'ELGEYO MARAKWET COUNTY'),
    (16, 'EMBU COUNTY'),
    (17, 'GARISSA COUNTY'),
    (18, 'HOMA BAY COUNTY'),
    (19, 'ISIOLO COUNTY'),
    (20, 'KAKAMEGA COUNTY'),
    (21, 'KERICHO COUNTY'),
    (22, 'KIAMBU COUNTY'),
    (23, 'KILIFI COUNTY'),
    (24, 'LAMU COUNTY'),
    (25, 'MACHINGA COUNTY'),
    (26, 'MANDERA COUNTY'),
    (27, 'MARSABIT COUNTY'),
    (28, 'MOMBASA COUNTY'),
    (29, 'MULANGO COUNTY'),
    (30, 'NAKURU COUNTY'),
    (31, 'NANDI COUNTY'),
    (32, 'NAROK COUNTY'),
    (33, 'NYANDARUA COUNTY'),
    (34, 'NYERI COUNTY'),
    (35, 'SAMBURU COUNTY'),
    (36, 'SIAYA COUNTY'),
    (37, 'TAITA TAVETA COUNTY'),
    (38, 'TANA RIVER COUNTY'),
    (39, 'THARAKA COUNTY'),
    (40, 'VIHIGA COUNTY'),
    (41, 'WAJIR COUNTY'),
    (42, 'WEST POKOT COUNTY'),
    (43, 'GOMBE COUNTY'),
    (44, 'BARINGO COUNTY'),
    (45, 'BOMET COUNTY'),
    (46, 'BUNGOMA COUNTY'),
    (47, 'BUSIA COUNTY'),
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


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
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


    