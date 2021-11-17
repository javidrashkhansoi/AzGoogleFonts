from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

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
    paginator = Paginator(fonts, 12, 6)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    return render(request, 'AzGoogleFonts/home.html', {'fonts': fonts, 'page_objects': page_objects})


def font(request, font_slug=None):
    user_text = request.GET.get('user_text')
    fonts = None
    designer = None
    font_group = None
    if font_slug is not None:
        fonts = AzGoogleFonts.objects.filter(slug=font_slug)
        try:
            for f in fonts:
                designer = AzGoogleFonts.objects.filter(designer=f.designer)
            paginator_for_designer = Paginator(designer, 4)
            page_number_designer = request.GET.get('page')
            designer_objects = paginator_for_designer.get_page(page_number_designer)
        except:
            pass
        try:
            for f in fonts:
                font_group = AzGoogleFonts.objects.filter(font_group=f.font_group)
            paginator_for_group = Paginator(font_group, 5)
            page_number_group = request.GET.get('page')
            group_objects = paginator_for_group.get_page(page_number_group)
        except:
            pass
    return render(request, 'AzGoogleFonts/font.html', {'fonts': fonts,
                                                       'user_text': user_text,
                                                       'designer': designer,
                                                       'font_group': font_group,
                                                       'designer_objects': designer_objects,
                                                       'group_objects': group_objects})


def search(request):
    search_text = request.GET.get('search')
    s_t = search_text.split(' ')
    fonts = None
    fonts_list = []
    if len(search_text) > 0:
        for f in AzGoogleFonts.objects.all():
            for st in s_t:
                if st.lower() in f.name.lower() and f.name not in [x.name for x in fonts_list]:
                    fonts_list.append(get_object_or_404(AzGoogleFonts, name=f.name))
                if st.lower() in f.designer.name.lower() and f.name not in [x.name for x in fonts_list]:
                    fonts_list.append(get_object_or_404(AzGoogleFonts, name=f.name, designer=f.designer))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    fonts = fonts_list
    paginator = Paginator(fonts, 12, 6)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    return render(request, 'AzGoogleFonts/search.html', {'fonts': fonts,
                                                         'page_objects': page_objects,
                                                         'search_text': search_text})
