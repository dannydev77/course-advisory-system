# Generated by Django 3.2.8 on 2022-05-31 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_application'),
        ('base', '0005_alter_application_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_application', to='users.profile'),
        ),
    ]
