# Generated by Django 3.0.8 on 2021-03-06 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0014_auto_20210304_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='namespace',
            field=models.CharField(default='399a32fb5cff43e5a6fd33f65577d60e', max_length=100),
        ),
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]