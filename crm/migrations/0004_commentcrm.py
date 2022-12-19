# Generated by Django 4.1.3 on 2022-12-19 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_statuscrm_alter_order_options_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Comment text')),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Date of creation')),
                ('comment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Request')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
