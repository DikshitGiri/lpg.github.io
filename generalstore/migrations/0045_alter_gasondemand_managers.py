# Generated by Django 4.0.1 on 2022-06-28 04:43

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0044_alter_gasondemand_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gasondemand',
            managers=[
                ('gasondemandmanager', django.db.models.manager.Manager()),
            ],
        ),
    ]
