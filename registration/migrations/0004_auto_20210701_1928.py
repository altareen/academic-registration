# Generated by Django 3.2.4 on 2021-07-01 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20210626_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='grade_level',
        ),
        migrations.AddField(
            model_name='user',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]