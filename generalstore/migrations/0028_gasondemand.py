# Generated by Django 4.0.1 on 2022-06-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0027_gasentry_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='gasondemand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_quantity', models.IntegerField(max_length=20)),
                ('customer_contact', models.IntegerField(max_length=10)),
                ('customer_address', models.CharField(max_length=100)),
                ('gas_category', models.CharField(max_length=30)),
            ],
        ),
    ]
