# Generated by Django 2.2.7 on 2020-02-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
