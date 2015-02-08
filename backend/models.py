from django.db import models


class Applicant(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255, blank=True)
    bedrooms = models.PositiveSmallIntegerField(null=True)
    income = models.PositiveIntegerField(null=True)

    def __str__(self):
        return "(%s) %s %s" % (self.id, self.name, self.phone_number)


class Property(models.Model):
    # this is the Twilio SMS number
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=1024)
    # this is the normal human contact number
    contact_phone = models.CharField(max_length=15)

    applicants = models.ManyToManyField(Applicant, blank=True)

    project_name = models.CharField(max_length=255, blank=True)
    agency = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    units = models.PositiveSmallIntegerField(default=0)
    ami30 = models.PositiveSmallIntegerField(default=0)
    ami50 = models.PositiveSmallIntegerField(default=0)
    ami60 = models.PositiveSmallIntegerField(default=0)
    ami80 = models.PositiveSmallIntegerField(default=0)
    studio = models.PositiveSmallIntegerField(default=0)
    br1 = models.PositiveSmallIntegerField(default=0)
    br2 = models.PositiveSmallIntegerField(default=0)
    br3 = models.PositiveSmallIntegerField(default=0)
    br4 = models.PositiveSmallIntegerField(default=0)
    br5 = models.PositiveSmallIntegerField(default=0)
    senior = models.BooleanField(default=False)

    def __str__(self):
        return "(%s) %s: %s applicants" %\
            (self.id, self.phone_number, self.applicants.count())

    class Meta:
        verbose_name_plural = "Properties"


