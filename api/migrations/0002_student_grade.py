# Generated by Django 3.0.5 on 2024-04-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]