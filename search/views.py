from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from search.models import Estate, Image
from search.forms import OrderForm, SearchForm


# Create your views here.
def index(request):
    latest = Estate.objects.all().order_by('-created')[:3]
    images = Image.objects.filter(estate__in=latest).distinct(
        'estate').order_by('-estate')

    context = {
        'images': images,
        'provinces': [prov for prov in enumerate(Estate.VALID_PROVINCES)],
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7),
        'bathrooms': range(1, 5),
        'garages': range(1, 4)
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'provinces': [prov for prov in enumerate(Estate.VALID_PROVINCES)],
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7),
        'bathrooms': range(1, 5),
        'garages': range(1, 4),
    }
    return render(request, 'about.html', context)


def properties(request):
    context = {}
    form = OrderForm(request.GET)
    if request.method == "POST":
        form = OrderForm(request.POST)
        #import pdb; pdb.set_trace()
        # Province
        province_selected = request.POST.get('city')
        context['province_selected'] = province_selected
        # Type
        transaction_type = request.POST.get('Type')
        context['transaction_type'] = transaction_type
        # Bedrooms
        bedrooms = request.POST.get('bedrooms', 0)
        context['bedrooms'] = bedrooms
        # garaje
        garage = request.POST.get('garage', 0)
        context['garage'] = garage
        # bathroom
        bathrooms = request.POST.get('bathrooms', 0)
        context['bathrooms'] = bathrooms
        # price
        price = request.POST.get('price')
        context['price'] = price
        # New Query:
        query = Estate.objects.filter(
            province=Estate.VALID_PROVINCES[int(province_selected)]
        ).order_by('-created')
        paginator = Paginator(query, 2)
        page_number = request.GET.get('page')
    else:
        value = request.GET.get('order', '1')
        context['value'] = value
        form = OrderForm(request.GET)
        if value == '1':
            query = Estate.objects.all().order_by('-created')
            paginator = Paginator(query, 2)
            page_number = request.GET.get('page')
        elif value == '2':
            query = Estate.objects.filter(transaction_type="Aquiler").order_by('-created')
            paginator = Paginator(query, 2)
            page_number = request.GET.get('page')
        else:
            query = Estate.objects.filter(transaction_type="Venta").order_by('-created')
            paginator = Paginator(query, 2)
            page_number = request.GET.get('page')
    try:
        estate_page = paginator.page(page_number)
    except PageNotAnInteger:
        estate_page = paginator.page(1)
    except EmptyPage:
        estate_page = paginator.page(paginator.num_pages)
    images = Image.objects.filter(estate__in=estate_page.object_list).distinct(
        'estate').order_by('-estate')

    context['images'] = images
    context['estates'] = estate_page
    context['form'] = form
    context['provinces'] = [prov for prov in enumerate(Estate.VALID_PROVINCES)]
    context['types'] = Estate.TRANSACTION_TYPE
    context['rooms'] = range(1, 7)
    context['bathrooms'] = range(1, 5)
    context['garages'] = range(1, 4)

    return render(request, 'property-grid.html', context)


def contact(request):
    context = {
        'provinces': [prov for prov in enumerate(Estate.VALID_PROVINCES)],
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7),
        'bathrooms': range(1, 5),
        'garages': range(1, 4)
    }
    return render(request, 'contact.html', context)


def property_single(request, id):
    estate = Estate.objects.get(id=id)
    images = Image.objects.filter(estate=estate)
    context = {
        'estate': estate,
        'images': images,
        'provinces': [prov for prov in enumerate(Estate.VALID_PROVINCES)],
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7),
        'bathrooms': range(1, 5),
        'garages': range(1, 4)
    }
    return render(request, 'property-single.html', context)
