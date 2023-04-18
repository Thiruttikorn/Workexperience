from enum import Enum
from datetime import datetime

from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils import timezone



time_format = '%Y-%m-%d %H:%H:%S'


class FutureValidator:
    
    def __call__(self, target):

        validate_result, reason  = self._future_validator(target)

        if not validate_result:
            raise ValidationError(reason)
        

    @staticmethod
    def _future_validator(target):
        start_time = target
        current_time = timezone.localtime()
        result = start_time > current_time
        reason = '' if result else f'Event was not scheduled for the future, {current_time} >= {start_time}'

        return result, reason
    

class NonOverlapValidator:
    
    def __call__(self, target_start, target_end, target_category):

        validate_result, reason  = self._non_overlap_validator(target_start, target_end, target_category)

        if not validate_result:
            raise ValidationError(reason)
        

    @staticmethod
    def _non_overlap_validator(target_start, target_end, target_category):
        from eventApp.models import Events

        overlap_lookup = Q(Event_category=target_category) & Q(Event_startTime__lte=target_end) & Q(Event_endTime__gte=target_start)
       
        query_set = Events.objects.filter(overlap_lookup)
        # raise RuntimeError(query_set)
        result = not query_set.exists()
        reason = '' if result else 'Scheduling an overlap period is not supported'

        return result, reason


from django.utils.translation import gettext_lazy as _
from eventApp.role import Role 
from eventApp.models import Events, Categorys, Users

class validate_user:
    def validate_role(value):
        for enum in Role:
            if enum.value == value:
                break
        else:
            raise ValidationError(_(' role does not exist in the system.'))

        
    def validate_null_name(value):
        if value is None:
            raise ValidationError(_('User - Name is None.'))

    def validate_null_email(value):
        if value is None:
            raise ValidationError(_('User - Email is None.'))

    def validate_LENGTH_name(value):
        if len(value) > 100:
            raise ValidationError(_('User - Name string is grater then 100.'))

    def validate_LENGTH_email(value):
        if len(value) > 50:
            raise ValidationError(_('User - Email string is grater then 50.'))

    def validate_WhiteSpace(value):
        if value.startswith(" "):
            raise ValidationError(_('User -  %s has whitespace.')% value)
        elif value.endswith(" "):
            raise ValidationError(_('User -  %s has whitespace.')% value)


    def validate_uniqueness_name(value):
        for u in Users.objects.raw('SELECT id, username FROM eventApp_users;'):
            if u.username == value:
                raise ValidationError(_('User -  %s has uniqueness.')% value)

    def validate_uniqueness_email(value):
        for u in Users.objects.raw('SELECT id, email FROM eventApp_users;'):
            if u.email == value:
                raise ValidationError(_('User -  %s has uniqueness.')% value)
    
    def validate_null_password(value):
        if value is None:
            raise ValidationError(_('User - Password is None.'))

    def validate_LENGTH_password(value):
        if len(value) > 14 or len(value) < 8:
            raise ValidationError(_('User - Password must length 8 to 14 characters'))

        