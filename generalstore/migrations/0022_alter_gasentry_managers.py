# Generated by Django 4.0.1 on 2022-06-02 10:32

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0021_remove_gasentry_firm_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gasentry',
            managers=[
                ('gasentrymanager', django.db.models.manager.Manager()),
            ],
        ),
    ]