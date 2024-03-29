# Generated by Django 3.2.16 on 2023-03-19 11:39

import django.db.models.deletion
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='Name of event')),
                ('description', models.TextField(verbose_name='Description of event')),
                ('address', models.TextField(verbose_name='Address/link of event')),
                ('datetime_spending', models.DateTimeField(verbose_name="Event's time spending")),
                ('is_online', models.BooleanField(default=False, verbose_name='Is online event')),
                ('is_private', models.BooleanField(default=False, verbose_name='Is private event')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Is finished event')),
                ('members', models.ManyToManyField(related_name='events_member', to=settings.AUTH_USER_MODEL, verbose_name='Members of event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_owner', to=settings.AUTH_USER_MODEL, verbose_name='Owner of event')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='Accept user invite or not')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active invite or not')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event', verbose_name='Event of invite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to=settings.AUTH_USER_MODEL, verbose_name='User of invite')),
            ],
            options={
                'verbose_name': 'Invite',
                'verbose_name_plural': 'Invites',
            },
        ),
    ]
