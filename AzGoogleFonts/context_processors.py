from .models import AzGoogleFonts, FontGroups, FontDesigners
from .views import home


def designers(request):
    designer_links = FontDesigners.objects.all()
    return dict(designer_links=designer_links)


def font_groups(request):
    font_groups_links = FontDesigners.objects.all()
    return dict(font_groups_links=font_groups_links)
