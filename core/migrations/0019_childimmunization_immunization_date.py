# Generated by Django 4.0.4 on 2022-06-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_vaccines_duration_given_alter_vaccines_time_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='childimmunization',
            name='immunization_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
