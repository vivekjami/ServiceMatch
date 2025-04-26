from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import User, Profile, Review, Quote
from .serializers import UserSerializer, ProfileSerializer, ReviewSerializer, QuoteSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

class SearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.filter(user__role='expert')
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'expertise']
    permission_classes = [IsAuthenticated]
    
    
    
    
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
import os

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chatbot(request):
    query = request.data.get('query')
    response = requests.post(
        'https://api-inference.huggingface.co/models/facebook/bart-large-mnli',
        headers={'Authorization': f'Bearer {os.getenv("HUGGING_FACE_API_KEY")}'},
        json={'inputs': query, 'parameters': {'candidate_labels': ['search help', 'profile help', 'general']}}
    )
    result = response.json()
    top_label = result['labels'][result['scores'].index(max(result['scores']))]
    return Response({'answer': f'Looks like you need help with {top_label}. Please clarify!'})