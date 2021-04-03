# Generated by Django 3.1.7 on 2021-04-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210401_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('npi', models.CharField(default='', max_length=10)),
                ('entity', models.CharField(default='', max_length=10, verbose_name='Entity code')),
                ('first_name', models.CharField(default='', max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(default='', max_length=50, verbose_name='Last Name')),
                ('organization', models.CharField(default='', max_length=255)),
                ('postal_code', models.CharField(default='', max_length=50, verbose_name='Postal Code')),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=40, verbose_name='State')),
                ('address', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=255)),
                ('telephone_number', models.CharField(default='', max_length=50)),
                ('mail_postal_code', models.CharField(default='', max_length=50)),
                ('mail_city', models.CharField(default='', max_length=50)),
                ('mail_state', models.CharField(default='', max_length=40)),
                ('mail_address', models.CharField(default='', max_length=255)),
                ('mail_country', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(default='', max_length=255)),
                ('sole_proprietor', models.CharField(default='', max_length=255)),
                ('enumeration_date', models.CharField(default='', max_length=255)),
                ('certification_date', models.CharField(default='', max_length=255)),
                ('tax_code', models.CharField(default='', max_length=255)),
                ('tax_group', models.CharField(default='', max_length=255)),
                ('tax_defintion', models.CharField(default='', max_length=5000)),
                ('tax_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='search',
        ),
    ]
