# Generated by Django 4.2.7 on 2023-12-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0013_delete_tbl_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='ChatFiles/')),
            ],
        ),
    ]
