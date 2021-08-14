from registration.models import *
from taxfiling.models import *
from othernavs.models import Registration as othernavreg

def regfunc(request):
    Registrations = Registration.objects.all()
    othernavregob = othernavreg.objects.all()
    tfiling = TaxFiling.objects.all()
    res= {
       'Registrations':Registrations,
       'othernavreg':othernavregob,
       'tfiling':tfiling,

    }
    return res