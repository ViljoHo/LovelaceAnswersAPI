from rest_framework.permissions import BasePermission
import hashlib
from api_keys.models import APIKey

class HasAPIKeyPermission(BasePermission):


  def has_permission(self, request, view):
    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
      return False
    
    raw_key = auth_header.split(" ")[1]

    hashed_key = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()

    try:
      api_key_obj = APIKey.objects.get(key=hashed_key)
    except APIKey.DoesNotExist:
      return False
    
    if request.method == "GET" and api_key_obj.level in ["read", "write", "admin"]:
        return True
    elif request.method == "POST" and api_key_obj.level in ["write", "admin"]:
        return True
    elif request.method in ["PUT", "DELETE"] and api_key_obj.level == "admin":
        return True
    
    return False