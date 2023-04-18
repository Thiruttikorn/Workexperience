
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _


from eventApp.models import Events, Categorys, Users
from eventApp.serializers import CategorysSerializer, EventsSerializer, UsersSerializer, UsersMatchSerializer
from eventApp.validators import FutureValidator, NonOverlapValidator, validate_user

from argon2.exceptions import VerifyMismatchError
from argon2 import PasswordHasher

from DjangoAPI.settings import SECRET_KEY
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from eventApp.token_permission import IsTokenValid
from eventApp.user_permission import IsUser
import jwt

@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
@csrf_exempt
@permission_classes([IsUser])
def usersApi(request, id=None):
    if request.user.is_authenticated:
        header_string  = request.headers['Authorization']
        token = header_string.replace('Bearer ','')
        decoded = jwt.decode(token, options={"verify_signature": False})
        role = decoded['role']
        if role == 'Admin':
            if request.method == 'GET':
                if id:
                    return detailUserApi(id)
                users = Users.objects.all().order_by('username')
                users_serializer = UsersSerializer(users, many=True, fields=(
                    'id', 'username', 'email', 'role', 'createdOn', 'updatedOn'))

                return JsonResponse(users_serializer.data, safe=False, status=status.HTTP_200_OK)

            elif request.method == 'POST':
                user_data = JSONParser().parse(request)
                users_serializer = UsersSerializer(data=user_data)

                user_email = user_data['email']
                user_name = user_data['username']
                user_role = user_data['role']
                user_password = user_data['password']

                email_validator = EmailValidator()

                try:
                    validate_user.validate_null_name(user_name)
                    validate_user.validate_null_email(user_email)
                    validate_user.validate_null_password(user_password)
                    validate_user.validate_LENGTH_email(user_email)
                    validate_user.validate_LENGTH_name(user_name)
                    validate_user.validate_LENGTH_password(user_password)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    email_validator(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    validate_user.validate_WhiteSpace(user_name)
                    validate_user.validate_WhiteSpace(user_email)
                    validate_user.validate_uniqueness_name(user_name)
                    validate_user.validate_uniqueness_email(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    validate_user.validate_role(user_role)
                except ValidationError as exc:
                    return JsonResponse("User - "+user_data['role']+exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                ph = PasswordHasher()
                user_data['password'] = ph.hash(user_data['password'])

                if users_serializer.is_valid():
                    users_serializer.save()
                    return JsonResponse("User - Added Successfully", safe=False, status=status.HTTP_200_OK)
                return JsonResponse("User - Failed to Add", safe=False)

            elif request.method == 'DELETE':
                user = Users.objects.get(id=id)
                user.delete()
                return JsonResponse("User - Deleted Successfully", safe=False, status=status.HTTP_200_OK)

            elif request.method == 'PUT':
                user_data = JSONParser().parse(request)
                user = Users.objects.get(id=user_data['id'])
                users_serializer = UsersSerializer(user, data=user_data)

                user_email = user_data['email']
                user_name = user_data['username']
                user_role = user_data['role']

                email_validator = EmailValidator()

                try:
                    validate_user.validate_null_name(user_name)
                    validate_user.validate_null_email(user_email)
                    validate_user.validate_LENGTH_email(user_email)
                    validate_user.validate_LENGTH_name(user_name)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    email_validator(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    validate_user.validate_WhiteSpace(user_name)
                    validate_user.validate_WhiteSpace(user_email)
                    validate_user.validate_uniqueness_name(user_name)
                    validate_user.validate_uniqueness_email(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    validate_user.validate_role(user_role)
                except ValidationError as exc:
                    return JsonResponse("User - "+user_data['role']+exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if users_serializer.is_valid():
                    users_serializer.save()
                    return JsonResponse("User - Updated Successfully", safe=False, status=status.HTTP_200_OK)
                return JsonResponse(users_serializer.errors, safe=False, status=status.http_400_bad_request)

            elif request.method == 'PATCH':
                user_data = JSONParser().parse(request)
                user = Users.objects.get(id=user_data['id'])
                users_serializer = UsersSerializer(user, data=user_data, partial=True)

                user_email = user_data['email']
                user_name = user_data['username']
                user_role = user_data['role']

                email_validator = EmailValidator()

                try:
                    validate_user.validate_null_name(user_name)
                    validate_user.validate_null_email(user_email)
                    validate_user.validate_LENGTH_email(user_email)
                    validate_user.validate_LENGTH_name(user_name)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    email_validator(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    validate_user.validate_WhiteSpace(user_name)
                    validate_user.validate_WhiteSpace(user_email)
                    validate_user.validate_uniqueness_name(user_name)
                    validate_user.validate_uniqueness_email(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    validate_user.validate_role(user_role)
                except ValidationError as exc:
                    return JsonResponse("User - "+user_data['role']+exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if users_serializer.is_valid():
                    users_serializer.save()
                    return JsonResponse("User - Updated Successfully", safe=False, status=status.HTTP_200_OK)
                return JsonResponse(users_serializer.errors, safe=False, status=status.http_400_bad_request)
            else:
                return JsonResponse("User - Cannot access", safe=False,status=status.HTTP_403_FORBIDDEN)
        return JsonResponse("User - Cannot access", safe=False,status=status.HTTP_403_FORBIDDEN)
    else:
        return JsonResponse("User - Cannot access", safe=False,status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@csrf_exempt
@permission_classes([IsUser])
def detailUserApi(request, id):
    if request.user.is_authenticated:
        header_string  = request.headers['Authorization']
        token = header_string.replace('Bearer ','')
        decoded = jwt.decode(token, options={"verify_signature": False})
        role = decoded['role']
        if role == 'Admin':
                    if request.method == 'GET':
                        users = Users.objects.get(id=id)
                        users_serializer = UsersSerializer(users, fields=(
                             'id', 'username', 'email', 'role', 'createdOn', 'updatedOn'))
                        return JsonResponse(users_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse("User - Cannot access1", safe=False,status=status.HTTP_403_FORBIDDEN)
        else:
            return JsonResponse("User - Cannot access2", safe=False,status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsUser])
def usersMatch(request, id=None):
    if request.user.is_authenticated:
        header_string  = request.headers['Authorization']
        token = header_string.replace('Bearer ','')
        decoded = jwt.decode(token, options={"verify_signature": False})
        role = decoded['role']
        if role == 'Admin':
            if request.method == 'POST':
                user_data = JSONParser().parse(request)
                user_email = user_data['email']
                user_password = user_data['password']
                email_validator = EmailValidator(user_email)
                try:
                    email_validator(user_email)
                    validate_user.validate_WhiteSpace(user_email)
                    validate_user.validate_null_email(user_email)
                    validate_user.validate_LENGTH_email(user_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)
                users = Users.objects.raw(
                    'SELECT id, username, email, password FROM eventApp_users;')
                for user in users:
                    if user.email == user_email:
                        ph = PasswordHasher()
                        try:
                            ph.verify(user.password, user_password)
                            return JsonResponse("User - Password Matched.", safe=False, status=status.HTTP_200_OK)
                        except VerifyMismatchError:
                            return JsonResponse("User - Password NOT Matched.", safe=False, status=status.HTTP_401_UNAUTHORIZED)
                return JsonResponse("User - A user with the specified email DOES NOT exist.", safe=False, status=status.HTTP_404_NOT_FOUND)
        else: 
            return JsonResponse("User - Cannot access", safe=False,status=status.HTTP_403_FORBIDDEN)
    else: 
        return JsonResponse("User - Cannot access", safe=False,status=status.HTTP_403_FORBIDDEN)

@csrf_exempt
def login(request, id=None):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_email = user_data['email']
        user_password = user_data['password']
        email_validator = EmailValidator()
        try:
            email_validator(user_email)
            validate_user.validate_WhiteSpace(user_email)
            validate_user.validate_null_email(user_email)
            validate_user.validate_LENGTH_email(user_email)
            validate_user.validate_LENGTH_password(user_password)
            validate_user.validate_null_password(user_password)
        except ValidationError as exc:
            return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)
        users = Users.objects.raw(
            'SELECT id, username, email, password FROM eventApp_users;')
        for user in users:
            if user.email == user_email:
                ph = PasswordHasher()
                try:
                    ph.verify(user.password, user_password)
                    token = RefreshToken.for_user(user)
                    token['role'] = user.role
                    token['email'] = user.email
                    return JsonResponse({'Status': "Login Successful", 'Email': user.email, 'Role': user.role, 'Token': str(token.access_token), 'Refresh': str(token)}, safe=False, status=status.HTTP_200_OK)
                except VerifyMismatchError:
                    return JsonResponse({'Status': "User - Password Incorrect."}, safe=False, status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({'Status': "User - A user with the specified email DOES NOT exist."}, safe=False, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def logout(request, id=None):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data = data['refresh']
        token = RefreshToken(data)
        token.blacklist()
        return JsonResponse({'Status' : "Successful Logout"},status=status.HTTP_205_RESET_CONTENT)



