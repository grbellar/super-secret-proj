# Generated by Django 4.2.5 on 2024-01-29 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Question Choice',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='exams.category')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=500, null=True)),
                ('choice_text', models.CharField(blank=True, max_length=500, null=True)),
                ('question', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.question')),
                ('selected_choice', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.choice')),
            ],
        ),
        migrations.CreateModel(
            name='UserExamState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, max_length=300, null=True)),
                ('current_question_index', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('graded', models.BooleanField(default=False)),
                ('score', models.FloatField(blank=True, null=True)),
                ('num_correct', models.IntegerField(blank=True, null=True)),
                ('num_questions', models.IntegerField(blank=True, null=True)),
                ('answers', models.ManyToManyField(through='exams.UserAnswer', to='exams.question')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.exam')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Exam',
                'unique_together': {('user', 'exam')},
            },
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user_exam_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='exams.userexamstate'),
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams', to='exams.examtype'),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(blank=True, to='exams.question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='exams.question'),
        ),
        migrations.AddField(
            model_name='category',
            name='exam_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='exams.examtype'),
        ),
    ]
