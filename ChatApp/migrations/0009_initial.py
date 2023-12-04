# Generated by Django 4.2.7 on 2023-12-02 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0001_initial'),
        ('ChatApp', '0008_delete_tbl_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_content', models.CharField(max_length=500)),
                ('chat_time', models.DateTimeField()),
                ('chat_file', models.FileField(upload_to='ChatFiles/')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to='Guest.tbl_user')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to='Guest.tbl_user')),
            ],
        ),
    ]
