# Generated by Django 3.2.25 on 2024-06-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('loginId', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('dob', models.DateField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sos_user',
            },
        ),
    ]
