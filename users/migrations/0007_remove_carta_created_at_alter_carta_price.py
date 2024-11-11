# Generated by Django 5.1.1 on 2024-11-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_carta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carta',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='carta',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
