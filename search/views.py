from django.shortcuts import render
from search.models import Estate, Image


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
    images = Image.objects.filter(estate__in=latest).distinct(
        'estate').order_by('-estate')

    context = {
        'images': images
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
