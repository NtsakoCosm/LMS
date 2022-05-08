# Generated by Django 3.2.4 on 2021-07-25 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0011_auto_20210726_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('chapter', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.chapter')),
                ('module', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.module')),
                ('objective', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.objective')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('concept', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.concept')),
                ('quiz', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('section', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.section')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.choice')),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
    ]
