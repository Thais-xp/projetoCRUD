# Generated by Django 4.1.3 on 2022-11-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
