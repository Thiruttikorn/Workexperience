from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.permissions import BasePermission
import jwt

class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        import logging
        user_id = request.user.id   
        header_string  = request.headers['Authorization']
        token = header_string.replace('Bearer ','')
        logging.warning(token)
        decoded = jwt.decode(token, options={"verify_signature": False})
        logging.warning(decoded)
        is_allowed_user = True
        try:
            is_blackListed = OutstandingToken.objects.get(user=user_id, token=token)
            if is_blackListed:
                is_allowed_user = False
        except OutstandingToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user