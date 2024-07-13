# api_key/urls.py
from django.urls import path
from .views import GenerateAPIKeyView, RefreshAPIKeyView, ValidateAPIKeyView

urlpatterns = [
    path('generate/', GenerateAPIKeyView.as_view(), name='generate_api_key'),
    path('refresh/', RefreshAPIKeyView.as_view(), name='refresh_api_key'),
    path('validate/', ValidateAPIKeyView.as_view(), name='validate_api_key'),
]
