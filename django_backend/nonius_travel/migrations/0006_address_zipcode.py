# Generated by Django 4.2.6 on 2023-10-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonius_travel', '0005_alter_address_country_alter_clients_birthdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=255, null=True),
        ),
    ]