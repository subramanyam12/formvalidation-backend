# Generated by Django 5.0 on 2023-12-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formvalidapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]