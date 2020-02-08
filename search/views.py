from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from search.models import Estate, Image
from search.forms import OrderForm


# Create your views here.
def index(request):
    latest = Estate.objects.all().order_by('-created')[:3]
    images = Image.objects.filter(estate__in=latest).distinct(
        'estate').order_by('-estate')

    context = {
        'images': images
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def properties(request):
    context = {}
    query = Estate.objects.all().order_by('-created')
    paginator = Paginator(query, 2)
    page_number = request.GET.get('page')
    form = OrderForm(request.GET)
    if request.GET:
        value = request.GET['order']
        context['value'] = value
        if value == OrderForm.TYPE_CHOICES[0][0]:
            pass
        elif value == OrderForm.TYPE_CHOICES[1][0]:
            query = Estate.objects.filter(transaction_type="Aquiler").order_by('-created')
            paginator = Paginator(query, 2)
            page_number = request.GET.get('page')
        elif value == OrderForm.TYPE_CHOICES[2][0]:
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

    return render(request, 'property-grid.html', context)


def contact(request):
    return render(request, 'contact.html')


def property_single(request, id):
    estate = Estate.objects.get(id=id)
    images = Image.objects.filter(estate=estate)
    context = {
        'estate': estate,
        'images': images
    }
    return render(request, 'property-single.html', context)
