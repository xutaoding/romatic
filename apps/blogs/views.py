from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.views.generic import View

from .models import Entry


# Create your views here.
class ShowEntryView(View):
    model = Entry
    template_name = 'mytest.html'

    def get(self, request):
        return render_to_response(self.template_name, context={'name': 102010})

        # data = self.model.objects.all()
        # return HttpResponse(data)

