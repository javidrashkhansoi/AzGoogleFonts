from .models import FontGroups


def font_groups_links(request):
    font_groups = FontGroups.objects.all()
    return dict(font_groups=font_groups)
