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
    latest = Estate.objects.all().order_by('-created')
    paginator = Paginator(latest, 2)
    import pdb; pdb.set_trace()
    page_number = request.GET.get('name')
    page_number = request.GET.get('page')
    form = OrderForm()
    try:
        estate_page = paginator.page(page_number)
    except PageNotAnInteger:
        estate_page = paginator.page(1)
    except EmptyPage:
        estate_page = paginator.page(paginator.num_pages)
    images = Image.objects.filter(estate__in=estate_page.object_list).distinct(
        'estate').order_by('-estate')

    context = {
        'images': images,
        'estates': estate_page,
        'form': form,
    }
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
