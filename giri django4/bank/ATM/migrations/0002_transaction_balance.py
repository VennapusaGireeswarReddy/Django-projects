# Generated by Django 5.0.6 on 2024-06-06 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=2348000, max_digits=10),
            preserve_default=False,
        ),
    ]
