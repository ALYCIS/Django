# Generated by Django 4.1.3 on 2022-11-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]