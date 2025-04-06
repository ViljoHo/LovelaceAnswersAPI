from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
import hashlib
from api_keys.models import APIKey


class HasAPIKeyPermission(BasePermission):

    def has_permission(self, request, view):

        # auth_header = request.headers.get("Authorization")
        # if not auth_header or not auth_header.startswith("Bearer "):
        #     return False

        # raw_key = auth_header.split(" ")[1]

        # hashed_key = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()

        api_key_header = request.headers.get("X-API-KEY")
        if not api_key_header:
            raise PermissionDenied(
                detail="API key is missing. Header must be 'X-API-KEY'"
            )

        hashed_key = hashlib.sha256(api_key_header.encode('utf-8')).hexdigest()

        try:
            api_key_obj = APIKey.objects.get(key=hashed_key)
        except APIKey.DoesNotExist:
            raise PermissionDenied(detail="API key is missing or invalid.")

        if request.method in ["GET", "HEAD", "OPTIONS"] and api_key_obj.level in [
            "read",
            "write",
            "admin",
        ]:
            return True
        elif request.method in ["POST", "PUT", "PATCH"] and api_key_obj.level in [
            "write",
            "admin",
        ]:
            return True
        elif request.method in ["DELETE"] and api_key_obj.level == "admin":
            return True
        
        value = 1

        return False
