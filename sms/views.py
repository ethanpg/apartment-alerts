import re

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


def signup_handler(from_number, to_number, match):
    try:
        property = Property.objects.get(phone_number=to_number)
    except:
        return HttpResponseBadRequest("Unknown number '%s'." % to_number)

    property.applicants.create(
        phone_number=from_number,
        name=match.group('name'),
        bedrooms=int(match.group('rooms')),
        income=int(match.group('income').replace(',', ''))
    )

    response = twilio.twiml.Response()
    response.message(**{
        'to': from_number,
        'from': to_number,
        'msg': "Thank you %s. We will let you know when apartments open up." %
            match.group('name'),
    })

    return HttpResponse(response)


def alert_handler(from_number, to_number, match):
    try:
        property = Property.objects.get(phone_number=to_number)
    except:
        return HttpResponseBadRequest("Unknown number '%s'." % to_number)

    query = dict(
        bedrooms=int(match.group('rooms')),
        income__gte=int(match.group('income_min').replace(',', '')),
        income__lte=int(match.group('income_max').replace(',', ''))
    )

    message = "Unit opening at %s: %sCall %s." % (
        property.address,
        match.group('message') + ". ",
        property.contact_phone
    )

    response = twilio.twiml.Response()
    for applicant in property.applicants.filter(**query):
        print("sending to %s" % applicant.phone_number)
        response.message(**{
            'to': applicant.phone_number,
            'from': to_number,
            'msg': message
        })
    return HttpResponse(response)


SMS_ROUTES = [
    (re.compile(r'^signup (?P<name>[A-Za-z ]+), (?P<rooms>[0-9]) b[a-z]+ms?, \$?(?P<income>[0-9,]+)'),
     signup_handler),
    (re.compile(r'^alert (?P<rooms>[0-9]) b[a-z]+ms?, \$?(?P<income_min>[0-9,]+)-(?P<income_max>[0-9,]+). ?(?P<message>.*)$'),
     alert_handler)
]


@csrf_exempt
def inbound_route(request):
    try:
        if request.method == 'GET':
            params = request.GET
        else:
            params = request.POST

        to_number = params['To']
        from_number = params['From']
        body = params['Body']
    except:
        return HttpResponseBadRequest(
            "Expecting To, From and Body parameters.")

    for (regex, handler) in SMS_ROUTES:
        match = regex.match(body)
        if match:
            return handler(from_number, to_number, match)

    response = twilio.twiml.Response()
    response.message(**{
        'to': from_number,
        'from': to_number,
        'msg': "Couldn't parse message: '%s'" % body
    })

    return HttpResponse(response)
