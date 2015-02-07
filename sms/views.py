from django.http import HttpResponse

import twilio.twiml


def hello(request):
    r = twilio.twiml.Response()
    r.message("Hello from Apartment Alerts.")
    return HttpResponse(r)