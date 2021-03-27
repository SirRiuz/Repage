# Generated by Django 3.1.6 on 2021-02-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('namespace', models.CharField(default='da65505db94145fc838ec9e25510290d', max_length=100)),
                ('isAcces', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
