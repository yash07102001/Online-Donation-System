# Generated by Django 3.2.2 on 2021-05-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_donation_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
