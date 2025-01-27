# Generated by Django 3.1.5 on 2024-12-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='', max_length=100)),
                ('maximum_capacity', models.IntegerField()),
                ('current_enrolled', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('enrolled_courses', models.ManyToManyField(related_name='students', to='course_app.Course')),
            ],
        ),
    ]
