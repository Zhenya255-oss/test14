# Generated by Django 2.2.6 on 2019-12-20 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life_desc', models.CharField(max_length=2000)),
                ('way_desc', models.CharField(max_length=2000)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('account_type', models.CharField(choices=[('INF', 'Influencer'), ('ADV', 'Advertiser'), ('SUB', 'Subscriber')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField(max_length=200)),
                ('likecount', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.Post')),
                ('users_liked', models.ManyToManyField(to='carte.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='carte.UserProfile')),
                ('influencers', models.ManyToManyField(to='carte.UserProfile')),
            ],
        ),
    ]
