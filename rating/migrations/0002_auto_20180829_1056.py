# Generated by Django 2.1 on 2018-08-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='user_create',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user_edit',
            new_name='edit_time',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='fullname',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='nickname',
            new_name='pwd',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user_pass',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='ava',
        ),
        migrations.AddField(
            model_name='rating',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rating',
            name='cv_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
