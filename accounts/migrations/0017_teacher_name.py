# Generated by Django 3.1 on 2020-09-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200922_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
