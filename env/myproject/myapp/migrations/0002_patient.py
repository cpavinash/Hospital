# Generated by Django 5.0 on 2024-01-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('paswword', models.CharField(max_length=200)),
            ],
        ),
    ]
