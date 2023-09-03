from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # Add more user profile fields as needed

class CreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='creator_pictures/', blank=True, null=True)
    # Add more fields specific to creators (e.g., about, social media links, etc.)

class SubscriptionTier(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE)
    # Add more fields as needed, such as benefits, access control, and limits

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields for post-related data like images, videos, etc.

class Subscription(models.Model):
    supporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tier = models.ForeignKey(SubscriptionTier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Pledge(models.Model):
    supporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    creator = models.ForeignKey(CreatorProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
