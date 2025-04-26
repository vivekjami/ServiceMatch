from rest_framework import serializers
from .models import User, Profile, Review, Quote

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'role']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'expertise', 'ratings']

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)
    expert = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'expert', 'rating', 'comment', 'timestamp']

class QuoteSerializer(serializers.ModelSerializer):
    business = UserSerializer(read_only=True)
    expert = UserSerializer(read_only=True)
    class Meta:
        model = Quote
        fields = ['id', 'business', 'expert', 'description', 'status', 'timestamp']