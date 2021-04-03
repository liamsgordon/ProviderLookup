from django.shortcuts import render
from django.core.paginator import Paginator
from main.models import provider

def is_valid_queryparam(param):
    return param != '' and param is not None

def BootstrapFilterView(request):
    qs = provider.objects.all()
    firstname_query = request.GET.get('First_name_contains')
    Lastname_query = request.GET.get('Last_name_contains')
    city_query = request.GET.get('City')
    zip_query = request.GET.get('zip_exact')
    state_query = request.GET.get('State')
    taxonomy_query = request.GET.get('description')
    check = True
    doubleCheck = True

    if is_valid_queryparam(zip_query) is False and is_valid_queryparam(city_query) is False and is_valid_queryparam(Lastname_query) is False and is_valid_queryparam(firstname_query) is False and taxonomy_query == 'Choose...' and state_query == 'Choose...':
        check = False 
        qs = provider.objects.none()

    if firstname_query != '' and firstname_query is not None:
        qs = qs.filter(first_name=firstname_query.upper())
        doubleCheck = False

    if Lastname_query != '' and Lastname_query is not None:
        qs = qs.filter(last_name=Lastname_query.upper())
        doubleCheck = False

    if city_query != '' and city_query is not None:
        qs = qs.filter(city=city_query.upper())
        doubleCheck = False

    if zip_query != '' and zip_query is not None:
        qs = qs.filter(postal_code=zip_query)
        doubleCheck = False
    
    if state_query != '' and state_query is not None and state_query != 'Choose...':
        if is_valid_queryparam(zip_query) is False and is_valid_queryparam(city_query) is False and is_valid_queryparam(Lastname_query) is False and is_valid_queryparam(firstname_query) is False and taxonomy_query == 'Choose...':
            check = False
            qs = provider.objects.none()
        else:
            qs = qs.filter(state=state_query)

    if is_valid_queryparam(taxonomy_query) and taxonomy_query != 'Choose...':
        if is_valid_queryparam(zip_query) is False and is_valid_queryparam(city_query) is False and is_valid_queryparam(Lastname_query) is False and is_valid_queryparam(firstname_query) is False and state_query == 'Choose...':
            check = False
            qs = provider.objects.none()
        else:
            qs = qs.filter(taxonomy=taxonomy_query)

    if doubleCheck == True:
        qs = provider.objects.none()

    qs = qs.order_by('first_name')[:5000]

    p = Paginator(qs, 200)

    page_num = request.GET.get('page', 1)

    try:
        qs = p.page(page_num)
    except:
        qs= p.page(1)


    context = {
        'queryset': qs,
        'check': check,
    }
    return render(request, "bootstrap_form.html", context)

def info(request, slug):
    pro = provider.objects.get(npi=slug)

    context = {
        'provider': pro,
    }
    return render(request, "info.html", context)

