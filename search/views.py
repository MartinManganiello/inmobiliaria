from django.shortcuts import render
from search.models import Estate, Image


# Create your views here.
def index(request):
    latest = Estate.objects.all().order_by('-created')[:3]
    images = Image.objects.filter(estate__in=latest).distinct('estate')

    context = {
        'images': images
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
