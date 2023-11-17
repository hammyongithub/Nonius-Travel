# Generated by Django 4.2.6 on 2023-10-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonius_travel', '0003_address_name_contact_name_document_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='clients',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='clients',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='clients',
            new_name='client',
        ),
        migrations.AddField(
            model_name='clients',
            name='addressC',
            field=models.ManyToManyField(related_name='clients', to='nonius_travel.address'),
        ),
        migrations.AddField(
            model_name='clients',
            name='contactC',
            field=models.ManyToManyField(related_name='clients', to='nonius_travel.contact'),
        ),
        migrations.AddField(
            model_name='clients',
            name='documentC',
            field=models.ManyToManyField(related_name='clients', to='nonius_travel.document'),
        ),
    ]