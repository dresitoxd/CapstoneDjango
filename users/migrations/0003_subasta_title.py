# Generated by Django 5.1.1 on 2024-09-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_subasta_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subasta',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
