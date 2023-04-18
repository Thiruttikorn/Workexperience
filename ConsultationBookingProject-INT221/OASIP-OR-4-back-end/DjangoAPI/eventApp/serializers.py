from attr import fields
from rest_framework import serializers
from eventApp.models import Categorys,Events,Users
from drf_writable_nested.serializers import WritableNestedModelSerializer

class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorys
        fields=('Event_category_id','Event_category_name','Event_category_description','Event_duration')


class EventsSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    Event_category = CategorysSerializer()
    # Event_startTime = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model=Events
        fields=('Booking_id','Booking_name','Booking_email','Event_startTime','Event_endTime','Event_notes','Event_category')

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UsersSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model=Users
        fields=('id','username','email','password','role','createdOn','updatedOn')

class UsersMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('email','password')
