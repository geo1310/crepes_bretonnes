# Generated by Django 3.0.3 on 2020-02-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL à réduire')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_acces', models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")),
            ],
            options={
                'verbose_name': 'Mini URL',
                'verbose_name_plural': 'Minis URL',
            },
        ),
    ]
