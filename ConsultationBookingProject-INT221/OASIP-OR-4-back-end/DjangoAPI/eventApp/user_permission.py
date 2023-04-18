from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.permissions import BasePermission
import jwt


class IsUser(BasePermission):
    def has_permission(self, request, view): 
        if request.user.is_authenticated:
            header_string  = request.headers['Authorization']
            token = header_string.replace('Bearer ','')
            decoded = jwt.decode(token, options={"verify_signature": False})['role']
            if decoded == 'Admin':
                is_allowed_user = True
            elif decoded == 'Student':
                is_allowed_user = True
            elif decoded == 'Lecturer':
                is_allowed_user = True
            else:
                is_allowed_user = False
            return is_allowed_user
        else:
            is_allowed_user = True
            return is_allowed_user
