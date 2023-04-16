from django.conf import settings
from django.http import HttpResponseNotFound
from django.template import loader

class Custom404Middleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.DEBUG and response.status_code == 404:
            template = loader.get_template('404.html')
            return HttpResponseNotFound(template.render())
        return response