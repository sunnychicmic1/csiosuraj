# Generated by Django 5.0.2 on 2024-02-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='allottee_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Allottee Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='house_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='House No.'),
        ),
    ]
