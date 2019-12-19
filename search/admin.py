from django.contrib import admin
from search.models import Estate, Image


class ImageInline(admin.StackedInline):
    model = Image
    max_num = 10
    extra = 0


class EstateAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)


admin.site.register(Estate, EstateAdmin)
admin.site.register(Image)
