from django.views import View
from django.http import JsonResponse
from .services import UserService
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

user_service = UserService()

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            name = data.get("name")
            email = data.get("email")
            if not name or not email:
                return JsonResponse({"error": "Name and email required"}, status=400)
            user = user_service.create_user(name, email)
            return JsonResponse({"id": user.id, "name": user.name, "email": user.email}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(View):
    def get(self, request, user_id):
        user = user_service.get_user(user_id)
        if user:
            return JsonResponse({"id": user.id, "name": user.name, "email": user.email})
        return JsonResponse({"error": "User not found"}, status=404)

    def post(self, request, user_id):  # Update
        try:
            data = json.loads(request.body.decode("utf-8"))
            name = data.get("name")
            email = data.get("email")
            user = user_service.update_user(user_id, name, email)
            if user:
                return JsonResponse({"id": user.id, "name": user.name, "email": user.email})
            return JsonResponse({"error": "User not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def delete(self, request, user_id):
        deleted = user_service.delete_user(user_id)
        if deleted:
            return JsonResponse({"message": "User deleted"})
        return JsonResponse({"error": "User not found"}, status=404)
