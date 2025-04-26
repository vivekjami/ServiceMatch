from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    auth0_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=[('business', 'Business'), ('expert', 'Expert')])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=255)
    expertise = models.CharField(max_length=255, blank=True, null=True)
    ratings = models.FloatField(default=0.0)

class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='reviews_given', on_delete=models.CASCADE)
    expert = models.ForeignKey(User, related_name='reviews_received', on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Quote(models.Model):
    business = models.ForeignKey(User, related_name='quotes_sent', on_delete=models.CASCADE, limit_choices_to={'role': 'business'})
    expert = models.ForeignKey(User, related_name='quotes_received', on_delete=models.CASCADE, limit_choices_to={'role': 'expert'})
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    timestamp = models.DateTimeField(auto_now_add=True)