# Generated by Django 4.1.5 on 2023-02-02 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=50, verbose_name='State Name')),
                ('stateAbbreviation', models.CharField(max_length=3, verbose_name='State Abbreviaton')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attractionName', models.CharField(max_length=200, verbose_name='Attraction Name')),
                ('homeState', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_attractions.state', verbose_name='Home State')),
            ],
        ),
    ]
