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
        'provinces': Estate.VALID_PROVINCES,
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7)
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'provinces': Estate.VALID_PROVINCES,
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7)
    }
    return render(request, 'about.html', context)


def properties(request):
    context = {}
    if request.method == "POST":
        import pdb; pdb.set_trace()
        # Province
        province_selected = request.POST.get('province_selected')
        context['province_selected'] = province_selected
        # Type
        transaction_type = request.POST.get('transaction_type')
        context['transaction_type'] = transaction_type
        # Bedrooms
        bedrooms = request.POST.get('bedrooms', 0)
        context['bedrooms'] = bedrooms
        # garaje
        garaje = request.POST.get('garaje', 0)
        context['garaje'] = garaje
        # bathroom
        bathroom = request.POST.get('bathroom', 0)
        context['bathroom'] = bathroom
        # price
        price = request.POST.get('price')
        context['price'] = price

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
    context['provinces'] = Estate.VALID_PROVINCES
    context['types'] = Estate.TRANSACTION_TYPE
    context['rooms'] = range(1, 7)

    return render(request, 'property-grid.html', context)


def contact(request):
    context = {
        'provinces': Estate.VALID_PROVINCES,
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7)
    }
    return render(request, 'contact.html', context)


def property_single(request, id):
    estate = Estate.objects.get(id=id)
    images = Image.objects.filter(estate=estate)
    context = {
        'estate': estate,
        'images': images,
        'provinces': Estate.VALID_PROVINCES,
        'types': Estate.TRANSACTION_TYPE,
        'rooms': range(1, 7)
    }
    return render(request, 'property-single.html', context)
