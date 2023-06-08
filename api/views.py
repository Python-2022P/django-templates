from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


class HomeView(View):
    def get(self, request: HttpRequest, username: str):
        context = {
            'username': username
        }
        return render(request=request, template_name='home.html', context=context)