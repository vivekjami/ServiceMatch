from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, ReviewViewSet, QuoteViewSet, SearchViewSet, chatbot

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'quotes', QuoteViewSet)
router.register(r'search', SearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),
    path('chatbot/', chatbot, name='chatbot'),
]