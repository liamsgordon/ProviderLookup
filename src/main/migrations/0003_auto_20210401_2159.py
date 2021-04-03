# Generated by Django 3.1.7 on 2021-04-01 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210401_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='certification_date',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doc',
            name='country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='entity_code',
            field=models.CharField(default='', max_length=10, verbose_name='Entity code'),
        ),
        migrations.AddField(
            model_name='doc',
            name='enumeration_date',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='first_name',
            field=models.CharField(default='', max_length=50, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='doc',
            name='gender',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='last_name',
            field=models.CharField(default='', max_length=50, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='doc',
            name='mail_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='mail_city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doc',
            name='mail_country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='mail_postal_code',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='doc',
            name='mail_state',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='doc',
            name='organization',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='postal_code',
            field=models.CharField(default='', max_length=50, verbose_name='Postal Code'),
        ),
        migrations.AddField(
            model_name='doc',
            name='sole_proprietor',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='state',
            field=models.CharField(default='', max_length=40, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='doc',
            name='tax_code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='tax_defintion',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='doc',
            name='tax_group',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='tax_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doc',
            name='telephone_number',
            field=models.CharField(default='', max_length=50),
        ),
    ]