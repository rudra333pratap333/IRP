# Generated by Django 3.1.5 on 2021-01-26 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Incedoinc', '0004_auto_20210126_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='positionOwner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positionOwner', to='Incedoinc.employee'),
        ),
        migrations.AlterField(
            model_name='job',
            name='raisedByEmployee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='raisedByEmployee', to='Incedoinc.employee'),
        ),
    ]