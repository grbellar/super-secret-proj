# Generated by Django 4.2.5 on 2024-02-15 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_exam_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='active',
            new_name='is_active',
        ),
    ]
