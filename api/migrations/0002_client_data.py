# Generated by Django 3.2.3 on 2021-05-19 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.data'),
        ),
    ]
