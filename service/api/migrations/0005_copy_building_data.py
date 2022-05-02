# -*- coding: utf-8 -*-

from django.db import migrations, IntegrityError


def copy_building_data(apps, schema_editor):
    Apartment = apps.get_model('api', 'Apartment')
    Building = apps.get_model('api', 'Building')
    for apartment in Apartment.objects.all():
        building = None
        try:
            building = Building.objects.create(
                city=apartment.city,
                street=apartment.street,
                street_number=apartment.street_number,
                latitude=apartment.latitude,
                longitude=apartment.longitude,
                description="An apartment building"
            )
        except IntegrityError:  # Building already exists at the given address
            building = Building.objects.get(
                city=apartment.city,
                street=apartment.street,
                street_number=apartment.street_number,
            )
        finally:
            apartment.building = building
            apartment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220502_2205'),
    ]

    operations = [
        migrations.RunPython(copy_building_data, migrations.RunPython.noop)
    ]
