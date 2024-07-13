# api_key/views.py
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import APIKey
from .aes_util import  decrypt_value

class GenerateAPIKeyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Generate a new API key and save it
        try:
            api_key = APIKey.generate_and_save()
            return JsonResponse({
                'message': 'API key generated successfully',
                'api_key': api_key.key  
            })
        except Exception as e:
                    return JsonResponse({
                        'status': 'error',
                        'message': str(e)  # Return the error message if any exception occurs
                    }, status=500)
        
class RefreshAPIKeyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Retrieve encrypted API key from request header
        encrypted_token = request.headers.get('X-API-Key')

        if not encrypted_token:
            return HttpResponseBadRequest('API key header (X-API-Key) missing')

        # Decrypt the token
        decrypted_token = decrypt_value(encrypted_token)

        if decrypted_token:
            # Refresh API key logic
            api_key = APIKey.generate_and_save()
            return JsonResponse({'message': 'API key refresh successfully','refr_api_key': api_key.key})
        
        return JsonResponse({'error': 'Unable to refresh API key'})

class ValidateAPIKeyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Retrieve encrypted API key from request header
        encrypted_token = request.headers.get('X-API-Key')

        if not encrypted_token:
            return HttpResponseBadRequest('API key header (X-API-Key) missing')

        # Decrypt the token
        decrypted_token = decrypt_value(encrypted_token)

        if decrypted_token:
            # Validate the decrypted token
            if APIKey.objects.filter(key=encrypted_token).exists():
                return JsonResponse({'message': 'API key vlide ','valid': True})
        
        return JsonResponse({'valid': False})
