# Generated by Django 4.0.1 on 2022-06-27 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0042_remove_gasondemand_totalgas'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasondemand',
            name='specified_supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='generalstore.gasentry'),
        ),
    ]