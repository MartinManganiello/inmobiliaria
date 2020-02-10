from django.db import models
import random
import os


class Estate(models.Model):

    TRANSACTION_TYPE = [
        'Aquiler',
        'Venta',
    ]

    VALID_PROVINCES = [
        "Buenos Aires",
        "Catamarca",
        "Chaco",
        "Chubut",
        "Córdoba",
        "Corrientes",
        "Entre Ríos",
        "Formosa",
        "Jujuy",
        "La Pampa",
        "La Rioja",
        "Mendoza",
        "Misiones",
        "Neuquén",
        "Río Negro",
        "Salta",
        "San Juan",
        "Santa Cruz",
        "Santa Fe",
        "Santiago del Estero",
        "Tierra del Fuego",
        "Tucumán",
    ]

    transaction_type = models.CharField(
        max_length=8, choices=list(map(
            lambda op: (op, op), TRANSACTION_TYPE)
        )
    )
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    province = models.CharField(max_length=50, choices=list(map(
        lambda prov: (prov, prov), VALID_PROVINCES))
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField()
    surface = models.PositiveIntegerField()
    garage = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()

    def __str__(self):
        return str(self.address) + ": $" + str(self.price)


def get_filename_ext(filepath):
    """ Return a name file and extension file."""
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext
    )
    return "estates/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Image(models.Model):
    estate = models.ForeignKey(
        Estate,
        default=None,
        on_delete=models.CASCADE,
        related_name='estates'
    )
    image = models.ImageField(
        upload_to=upload_image_path, verbose_name='Image'
    )
