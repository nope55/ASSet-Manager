# Generated by Django 5.0.2 on 2024-03-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('teacher', models.CharField(max_length=32)),
            ],
        ),
    ]
