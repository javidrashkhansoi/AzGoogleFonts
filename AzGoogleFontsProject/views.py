from django.shortcuts import render, get_object_or_404


def page404(request, exception):
    return render(request, 'AzGoogleFonts/404.html', status=404)


def page500(request):
    return render(request, 'AzGoogleFonts/404.html', status=500)
