from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import twilio.twiml

from backend.models import Property, Applicant

@csrf_exempt
def hello(request):
    r = twilio.twiml.Response()
    r.message("Hello from Apartment Alerts.")
    return HttpResponse(r)


@csrf_exempt
def alert_applicants(request):
    try:
        if request.method == 'GET':
            params = request.GET
        else:
            params = request.POST

        to_number = params['To']
        from_number = params['From']
        body = params['Body']
    except:
        return HttpResponseBadRequest("No from number.")

    try:
        property = Property.objects.get(phone_number=to_number)
    except:
        return HttpResponseBadRequest("Unknown number '%s'." % to_number)

    response = twilio.twiml.Response()
    print("got property id %s" % property.id)
    for applicant in property.applicants.all():
        print("sending to %s" % applicant.phone_number)
        response.message(**{
            'to': applicant.phone_number,
            'from': to_number,
            'msg': body
        })

    return HttpResponse(response)
