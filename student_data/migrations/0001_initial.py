# Generated by Django 4.1 on 2023-03-03 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coursedata',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('sid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_data.coursedata')),
            ],
        ),
    ]
