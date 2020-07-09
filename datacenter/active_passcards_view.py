from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)
    visits = Visit.objects.filter(leaved_at__isnull=True)
    context = {
        "active_passcards": active_passcards,
        "visits": visits
    }

    return render(request, 'active_passcards.html', context)
