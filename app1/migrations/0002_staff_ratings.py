# Generated by Django 3.2 on 2023-03-17 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff_ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=255)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.staff_info')),
            ],
        ),
    ]
