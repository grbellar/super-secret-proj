# Generated by Django 4.2.5 on 2024-01-27 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_examtype_rename_question_exam_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='user_exam_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_answers', to='exams.userexamstate'),
        ),
    ]