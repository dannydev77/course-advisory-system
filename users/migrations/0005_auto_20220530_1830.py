# Generated by Django 3.2.8 on 2022-05-30 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_application_name'),
        ('users', '0004_auto_20220530_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='application',
        ),
        migrations.AddField(
            model_name='profile',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.application'),
        ),
    ]