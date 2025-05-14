from django.shortcuts import render


def page_not_found(request, exception):
    template = 'pages/404.html'
    return render(request, template, status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    template = 'pages/500.html'
    return render(request, template, status=500)
