# Generated by Django 4.0 on 2022-06-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_child_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/default-avatar.jpg', null=True, upload_to='profile_pictures/children/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=13),
        ),
    ]
