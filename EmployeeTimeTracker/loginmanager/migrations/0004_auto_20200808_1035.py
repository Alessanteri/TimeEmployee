# Generated by Django 3.0.8 on 2020-08-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginmanager', '0003_profile_rate_per_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rate_per_hour',
            field=models.FloatField(blank=True, null=True),
        ),
    ]