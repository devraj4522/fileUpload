# Generated by Django 4.0 on 2021-12-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileUploadApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to='books/'),
        ),
    ]
