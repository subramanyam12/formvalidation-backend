# Generated by Django 5.0 on 2023-12-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formvalidapp', '0002_alter_profile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]