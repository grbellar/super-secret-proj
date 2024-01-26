# Generated by Django 4.2.5 on 2024-01-21 19:56

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model("exams", "Exam")
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_exam_uuid'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]