from django.shortcuts import render, get_object_or_404
from .models import AzGoogleFonts, FontDesigners, FontGroups


def home(request, designer_slug=None, group_slug=None):
    fonts = None
    designer_page = None
    group_page = None
    if designer_slug is not None:
        designer_page = get_object_or_404(FontDesigners, slug=designer_slug)
        fonts = AzGoogleFonts.objects.filter(designer=designer_page)
    elif group_slug is not None:
        group_page = get_object_or_404(FontGroups, slug=group_slug)
        fonts = AzGoogleFonts.objects.filter(font_group=group_page)
    else:
        fonts = AzGoogleFonts.objects.all()
    return render(request, 'AzGoogleFonts/home.html', {'fonts': fonts})
