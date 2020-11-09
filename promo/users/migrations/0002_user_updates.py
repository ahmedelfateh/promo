# Generated by Django 3.0.11 on 2020-11-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Mobile Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('ADMINISTRATOR', 'Administrator'), ('NORMAL', 'Normal')], default='NORMAL', max_length=50, null=True, verbose_name='User Type'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]