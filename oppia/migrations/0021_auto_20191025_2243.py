# Generated by Django 2.2.5 on 2019-10-25 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0020_coursepublishinglog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepublishinglog',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oppia.Course'),
        ),
        migrations.AlterField(
            model_name='coursepublishinglog',
            name='new_version',
            field=models.BigIntegerField(null=True),
        ),
    ]