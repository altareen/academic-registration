# Generated by Django 3.2.4 on 2021-06-26 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='grade_level',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('capacity', models.IntegerField(default=0)),
                ('section', models.IntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='registration.department')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='registration.instructor')),
                ('students', models.ManyToManyField(blank=True, related_name='pupils', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]