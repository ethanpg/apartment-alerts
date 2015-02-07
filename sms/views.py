from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import twilio.twiml


@csrf_exempt
def hello(request):
    r = twilio.twiml.Response()
    r.message("Hello from Apartment Alerts.")
    return HttpResponse(r)