import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=100)
    county_no = models.PositiveSmallIntegerField(unique=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)+"-"+str(self.county_no)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Counties'
        ordering = ['county_no']

    def __str__(self):
        return self.name

class Hospital(models.Model):
    hospital_id = models.CharField(max_length=5, unique=True, blank=True, null=True)
    name = models.CharField(max_length=254)
    license_no = models.CharField(max_length=20, blank=True, null=True)
    county = models.ForeignKey(County, blank=True, null=True, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.name} -> { self.county }'

    def save(self, *args, **kwargs):
        try:
            get_id_of_previous_record = Hospital.objects.last().id
        except:
            get_id_of_previous_record = 0
        if not self.hospital_id:
            if self.id is None:
                if get_id_of_previous_record:
                    new_id = get_id_of_previous_record + 1
                    self.hospital_id = 'H' + str(new_id).zfill(4)
            else:
                self.hospital_id = 'H' + str(self.id).zfill(4)
        super().save(*args, **kwargs)