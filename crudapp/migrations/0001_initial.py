# Generated by Django 2.2 on 2021-09-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
