# Generated by Django 3.0.11 on 2020-11-09 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promos', to=settings.AUTH_USER_MODEL),
        ),
    ]
