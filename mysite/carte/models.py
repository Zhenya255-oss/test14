from django.db import models
from django.contrib.auth.models import (User, AbstractBaseUser,PermissionsMixin)
from django.contrib import admin
# Create your models here.

from django.forms import ModelForm



class UserProfile(models.Model):
    # This field is required.

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # These fields are optional
    life_desc = models.CharField(max_length=2000)
    way_desc = models.CharField(max_length=2000)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    INFLUENCER = 'INF'
    ADVERTISER = 'ADV'
    SUBSCRIBER = 'SUB'

    ACCOUNT_CHOICES = [
        (INFLUENCER, 'Influencer'),
        (ADVERTISER, 'Advertiser'),
        (SUBSCRIBER, 'Subscriber'),
    ]
    account_type = models.CharField (
        max_length=3,
        choices=ACCOUNT_CHOICES,
    )

    def __str__(self):
        return self.user.username


# Create your models here.

class AccountType(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Influencer(models.Model):
    influencers = models.ManyToManyField(UserProfile)
    current_user = models.ForeignKey(UserProfile, related_name = "owner", null =True, on_delete=models.CASCADE)

    @classmethod
    def add_influencer(cls, current_user, new_influencer):
        subscriber, created = cls.objects.get_or_create(current_user= current_user)
        subscriber.influencers.add(new_influencer)

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.IntegerField(blank=True, null=True)
    text = models.TextField(max_length=200)
    likecount = models.IntegerField (blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class Like(models.Model):
    users_liked = models.ManyToManyField(UserProfile)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #likecount = models.IntegerField(blank=True,null=True)



