# Generated by Django 4.2.10 on 2024-02-08 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_alter_locationdetails_address_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationdetails',
            unique_together={('business_title', 'address')},
        ),
    ]
