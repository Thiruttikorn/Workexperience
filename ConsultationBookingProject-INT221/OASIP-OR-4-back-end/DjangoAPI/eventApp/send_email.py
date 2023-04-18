from django.conf import settings
from django.core.mail import send_mail

from datetime import datetime
from datetime import timezone

def sending_event_email(serializer):
    Booking_name = serializer.data['Booking_name']
    Booking_email = serializer.data['Booking_email']
    Event_startTime = serializer.data['Event_startTime']
    datetime_object = datetime.strptime(Event_startTime, "%Y-%m-%dT%H:%M:%S%z")
    datetime_object = datetime_object.strftime("%a %b %d, %Y %H:%M %p")
    Event_endTime = serializer.data['Event_endTime'] 
    Event_endTime = datetime.strptime(Event_endTime, "%Y-%m-%dT%H:%M:%S%z")
    Event_endTime = Event_endTime.strftime("%H:%M %p")
    Event_notes = serializer.data['Event_notes']
    Event_category_id = serializer.data['Event_category']['Event_category_id']
    Event_category_name = serializer.data['Event_category']['Event_category_name']
    Event_duration = serializer.data['Event_category']['Event_duration']

    subject = f'[OASIP] {Event_category_name} @ {datetime_object} - {Event_endTime}'
    message = f'Booking Name: {Booking_name}\nEvent Category: {Event_category_name}\nWhen: {datetime_object} - {Event_endTime}\nEvent Notes: {Event_notes}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Booking_email,]
    send_mail( subject, message, email_from, recipient_list )


    # Subject: [OASIP] Server-side Clinic @ Mon Oct 24, 2022 16:00 - 16:30 (ICT) 
    # Reply-to: noreply@intproj21.sit.kmutt.ac.th
    # Booking Name:	PBI36 สมส่วน สุขศรี
    # Event Category: Server-side Clinic
    # When: Mon Oct 24, 2022 16:00 - 16:30 (ICT) 
    # Event Notes: