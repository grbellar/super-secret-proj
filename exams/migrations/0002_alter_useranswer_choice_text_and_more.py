# Generated by Django 4.2.5 on 2024-02-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='choice_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
