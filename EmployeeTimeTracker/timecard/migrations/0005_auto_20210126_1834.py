# Generated by Django 3.1.5 on 2021-01-26 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0004_dailylog_message_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylog',
            name='message_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timecard.messageobject'),
        ),
    ]