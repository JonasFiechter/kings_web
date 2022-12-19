from django.shortcuts import render
from profiles.models import Profile
from billing.models import Contract
from profiles.models import Profile
from datetime import datetime

def billing_view(request):
    contracts = Contract.objects.filter(owner=request.user.id)
    contracts_all = Contract.objects.all()

    user_full_name = Profile.objects.filter(username='admin')

    print(datetime.now().month)
    print(f'Contratos {contracts} ID => {request.user.id}')
    for contract in contracts_all:
        print(f'c ID => {contract.id} \
            r Year => {contract.reference_year} \
            jan => {contract.tuition_jan} \
            t => {contract.owner}')

    if Profile.objects.filter(email=request.user.id).exists():
        profile = Profile.objects.get(email=request.user.id)

    return render(request, 'billing/index.html', {
                                                    'profile': profile,
                                                    'contracts': contracts,
                                                    })