# Generated by Django 5.1.4 on 2025-03-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_taskmodel_due_data_taskmodel_priority_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='due_data',
            field=models.DateTimeField(null=True),
        ),
    ]
