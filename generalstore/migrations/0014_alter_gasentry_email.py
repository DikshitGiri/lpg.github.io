# Generated by Django 4.0.1 on 2022-06-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0013_alter_gasentry_complete_firm_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasentry',
            name='Email',
            field=models.EmailField(max_length=50, null=b'I01\n'),
        ),
    ]
