# Generated by Django 2.0.4 on 2018-09-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fono', models.IntegerField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]