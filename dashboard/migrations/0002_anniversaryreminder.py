# Generated by Django 4.2.20 on 2025-04-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnniversaryReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('recipient_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('recipient_email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('occasion', models.CharField(default='Birthday', max_length=100)),
            ],
        ),
    ]
