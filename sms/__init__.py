
from django.conf import settings

from twilio.rest import TwilioRestClient


twilio = TwilioRestClient(settings.TWILIO_SID, settings.TWILIO_AUTH)
