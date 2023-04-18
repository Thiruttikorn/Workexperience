
from tkinter import E
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from django.http import HttpResponseBadRequest
from soupsieve import escape
from eventApp.models import Events, Categorys, Users, Event_category_owner
from eventApp.serializers import CategorysSerializer, EventsSerializer, UsersSerializer
from eventApp.validators import FutureValidator, NonOverlapValidator,validate_user

from datetime import timedelta
from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from eventApp.user_permission import IsUser

import jwt

from eventApp.send_email import sending_event_email

time_format = '%Y-%m-%dT%H:%M'

@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
@csrf_exempt
@permission_classes([IsUser])
def eventApi(request, id=None):
    if request.user.is_authenticated:
        header_string = request.headers['Authorization']
        token = header_string.replace('Bearer ','')
        decoded = jwt.decode(token, options={"verify_signature": False})
        role = decoded['role']
        email = decoded['email']
        user_id = decoded['user_id'] 
        if role == 'Admin':
            if request.method == 'GET':
                if id:
                    return detailEventApi(id)
                events = Events.objects.all().order_by('-Event_startTime')
                events_serializer = EventsSerializer(events, many=True)
                return JsonResponse(events_serializer.data, safe=False,status=status.HTTP_200_OK)

            elif request.method == 'POST':
                events_data = JSONParser().parse(request)
                events_serializer = EventsSerializer(data=events_data)

                Event_category = events_data['Event_category']
                Event_duration = Event_category['Event_duration']
                Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
                Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

                Event_category = Event_category['Event_category_id']

                Booking_email = events_data['Booking_email']

                email_validator = EmailValidator()
                future_validator = FutureValidator()
                non_overlap_validator = NonOverlapValidator()

                try:
                    email_validator(Booking_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    future_validator(Event_startTime)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    non_overlap_validator(Event_startTime, Event_endTime, Event_category)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if events_serializer.is_valid():
                    events_serializer.save()
                    sending_event_email(events_serializer)
                    return JsonResponse("Event - Added Successfully", safe=False,status=status.HTTP_200_OK)
                return JsonResponse(events_serializer.errors, safe=False)

            elif request.method == 'PUT':
                events_data = JSONParser().parse(request)
                event = Events.objects.get(Booking_id=events_data['Booking_id'])
                events_serializer = EventsSerializer(event, data=events_data)

                Event_category = events_data['Event_category']
                Event_duration = Event_category['Event_duration']
                Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
                Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

                Event_category = Event_category['Event_category_id']

                Booking_email = events_data['Booking_email']

                email_validator = EmailValidator()
                future_validator = FutureValidator()
                non_overlap_validator = NonOverlapValidator()

                try:
                    email_validator(Booking_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    future_validator(Event_startTime)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    non_overlap_validator(Event_startTime, Event_endTime, Event_category)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if events_serializer.is_valid():
                    events_serializer.save()
                    return JsonResponse("Event - Updated Successfully", safe=False, status=status.HTTP_200_OK)
                return JsonResponse(events_serializer.errors, safe=False, status=status.http_400_bad_request)

            elif request.method == 'DELETE':
                event = Events.objects.get(Booking_id=id)
                event.delete()
                return JsonResponse("Event - Deleted Successfully", safe=False,status=status.HTTP_200_OK)

            elif request.method == 'PATCH':
                events_data = JSONParser().parse(request)
                event = Events.objects.get(Booking_id=events_data['Booking_id'])
                events_serializer = EventsSerializer(event, events_data, partial=True)

                Event_category = events_data['Event_category']
                Event_duration = Event_category['Event_duration']
                Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
                Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

                Event_category = Event_category['Event_category_id']

                Booking_email = events_data['Booking_email']

                email_validator = EmailValidator()
                future_validator = FutureValidator()
                non_overlap_validator = NonOverlapValidator()

                try:
                    email_validator(Booking_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    future_validator(Event_startTime)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    non_overlap_validator(Event_startTime, Event_endTime, Event_category)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if events_serializer.is_valid():
                    events_serializer.save()
                    return JsonResponse("Event - Updated Successfully", safe=False,status=status.HTTP_200_OK)
                return JsonResponse(events_serializer.errors, safe=False, status=status.http_400_bad_request)

        elif role == 'Student': 
            if request.method == 'GET':
                if id:
                    return detailEventApi(id)
                events = Events.objects.all().filter(Booking_email=email).order_by('-Event_startTime')
                events_serializer = EventsSerializer(events, many=True)
                return JsonResponse(events_serializer.data, safe=False,status=status.HTTP_200_OK)

            elif request.method == 'POST':
                events_data = JSONParser().parse(request)
                events_serializer = EventsSerializer(data=events_data)

                Event_category = events_data['Event_category']
                Event_duration = Event_category['Event_duration']
                Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
                Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

                Event_category = Event_category['Event_category_id']

                Booking_email = events_data['Booking_email']

                email_validator = EmailValidator()
                future_validator = FutureValidator()
                non_overlap_validator = NonOverlapValidator()

                try:
                    email_validator(Booking_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    future_validator(Event_startTime)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    non_overlap_validator(Event_startTime, Event_endTime, Event_category)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if email != Booking_email:
                    return JsonResponse("Event - Please enter this email account", safe=False,status=status.HTTP_400_BAD_REQUEST)

                if events_serializer.is_valid():
                    events_serializer.save()
                    sending_event_email(events_serializer)
                    return JsonResponse("Event - Added Successfully", safe=False,status=status.HTTP_200_OK)
                return JsonResponse(events_serializer.errors, safe=False)

            elif request.method == 'PUT':
                events_data = JSONParser().parse(request)
                event = Events.objects.get(Booking_id=events_data['Booking_id'])
                events_serializer = EventsSerializer(event, data=events_data)

                Event_category = events_data['Event_category']
                Event_duration = Event_category['Event_duration']
                Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
                Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

                Event_category = Event_category['Event_category_id']

                Booking_email = events_data['Booking_email']

                email_validator = EmailValidator()
                future_validator = FutureValidator()
                non_overlap_validator = NonOverlapValidator()

                try:
                    email_validator(Booking_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    future_validator(Event_startTime)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    non_overlap_validator(Event_startTime, Event_endTime, Event_category)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if email != Booking_email:
                    return JsonResponse("Event - This Email doesn't match with reserved email", safe=False,status=status.HTTP_403_FORBIDDEN)

                if events_serializer.is_valid():
                    events_serializer.save()
                    return JsonResponse("Event - Updated Successfully", safe=False, status=status.HTTP_200_OK)
                return JsonResponse(events_serializer.errors, safe=False, status=status.http_400_bad_request)

            elif request.method == 'DELETE':
                booking_id = Events.objects.raw('SELECT Booking_id, Booking_email FROM eventApp_Events WHERE Booking_id = id;')
                Booking_email = booking_id.Booking_email
                if email != Booking_email:
                    return JsonResponse("Event - This Email doesn't match with reserved email", safe=False,status=status.HTTP_403_FORBIDDEN)
                event = Events.objects.get(Booking_id=id)
                event.delete()
                return JsonResponse("Event - Deleted Successfully", safe=False,status=status.HTTP_200_OK)

            elif request.method == 'PATCH':
                events_data = JSONParser().parse(request)
                event = Events.objects.get(Booking_id=events_data['Booking_id'])
                events_serializer = EventsSerializer(event, events_data, partial=True)

                Event_category = events_data['Event_category']
                Event_duration = Event_category['Event_duration']
                Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
                Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

                Event_category = Event_category['Event_category_id']

                Booking_email = events_data['Booking_email']

                email_validator = EmailValidator()
                future_validator = FutureValidator()
                non_overlap_validator = NonOverlapValidator()

                try:
                    email_validator(Booking_email)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    future_validator(Event_startTime)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                try:
                    non_overlap_validator(Event_startTime, Event_endTime, Event_category)
                except ValidationError as exc:
                    return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

                if email != Booking_email:
                    return JsonResponse("Event - This Email doesn't match with reserved email", safe=False,status=status.HTTP_403_FORBIDDEN)

                if events_serializer.is_valid():
                    events_serializer.save()
                    return JsonResponse("Event - Updated Successfully", safe=False,status=status.HTTP_200_OK)
                return JsonResponse(events_serializer.errors, safe=False, status=status.http_400_bad_request)
        
        elif role == 'Lecturer': 
            if request.method == 'GET':
                from django.db.models import Q
                find_event_id = Events.objects.raw(
                    'SELECT E.Booking_id FROM eventApp_event_category_owner O JOIN eventApp_events E ON E.Event_category_id = O.Event_category_owner_category_id_id WHERE Event_category_owner_user_id_id = %d;' % user_id )
               
                event_id = []
                for x in find_event_id:
                    event_id.append(x.Booking_id)

                events = Events.objects.all().filter(Booking_id__in=event_id).order_by('-Event_startTime')
                events_serializer = EventsSerializer(events, many=True)
                return JsonResponse(events_serializer.data, safe=False,status=status.HTTP_200_OK)
            else:
                return JsonResponse("Event - Lecturer cannot add, edit, and delete events.", safe=False,status=status.HTTP_403_FORBIDDEN)
    else:
        if request.method == 'POST':
            events_data = JSONParser().parse(request)
            events_serializer = EventsSerializer(data=events_data)

            Event_category = events_data['Event_category']
            Event_duration = Event_category['Event_duration']
            Event_startTime = timezone.make_aware(datetime.strptime(events_data['Event_startTime'], time_format))
            Event_endTime = events_data['Event_endTime'] = Event_startTime + timedelta(minutes=Event_duration)

            Event_category = Event_category['Event_category_id']

            Booking_email = events_data['Booking_email']

            email_validator = EmailValidator()
            future_validator = FutureValidator()
            non_overlap_validator = NonOverlapValidator()

            try:
                email_validator(Booking_email)
            except ValidationError as exc:
                return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

            try:
                future_validator(Event_startTime)
            except ValidationError as exc:
                return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

            try:
                non_overlap_validator(Event_startTime, Event_endTime, Event_category)
            except ValidationError as exc:
                return JsonResponse(exc.message, status=status.HTTP_400_BAD_REQUEST, safe=False)

            if events_serializer.is_valid():
                events_serializer.save()
                sending_event_email(events_serializer)
                return JsonResponse("Event - Added Successfully", safe=False,status=status.HTTP_200_OK)
            return JsonResponse(events_serializer.errors, safe=False)
        return JsonResponse("Event - Guest cannot access", safe=False,status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@permission_classes([IsUser])
def categoryApi(request, id=0):
    if request.method == 'GET':
        categorys = Categorys.objects.all()
        categorys_serializer = CategorysSerializer(categorys, many=True)
        return JsonResponse(categorys_serializer.data, safe=False,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        categorys_data = JSONParser().parse(request)
        categorys_serializer = CategorysSerializer(data=categorys_data)
        if categorys_serializer.is_valid():
            categorys_serializer.save()
            return JsonResponse("Category - Added Successfully", safe=False,status=status.HTTP_200_OK)
        return JsonResponse(categorys_serializer.errors, safe=False)

    elif request.method == 'DELETE':
        category = Categorys.objects.get(Event_category_id=id)
        category.delete()
        return JsonResponse("Category - Deleted Successfully", safe=False ,status=status.HTTP_200_OK)
 

@csrf_exempt
@permission_classes([IsUser])
def detailEventApi(request, id):
    event = Events.objects.get(Booking_id=id)
    events_serializer = EventsSerializer(event)
    return JsonResponse(events_serializer.data, safe=False, status=status.HTTP_200_OK)


@csrf_exempt
@permission_classes([IsUser])
def detailCategoryApi(request,id):
    category = Categorys.objects.get(Event_category_id=id)
    categorys_serializer = CategorysSerializer(category)
    return JsonResponse(categorys_serializer.data, safe=False,status=status.HTTP_200_OK)

@csrf_exempt
@permission_classes([IsUser])
def eventsCategoryApi(request,id):
    event = Events.objects.filter(Event_category_id=id)
    events_serializer = EventsSerializer(event,many=True)
    return JsonResponse(events_serializer.data, safe=False,status=status.HTTP_200_OK)

