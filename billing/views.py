from django.shortcuts import render
from profiles.models import Profile
from billing.models import Contract

def billing_view(request):

    contracts = Contract.objects.filter(owner=request.user.id)
    print(f'Contratos {contracts} ID => {request.user.id}')

    if Profile.objects.filter(email=request.user.id).exists():
        profile = Profile.objects.get(email=request.user.id)

    return render(request, 'billing/index.html', {'profile': profile})