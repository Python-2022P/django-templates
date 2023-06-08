from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


class HomeView(View):
    def get(self, request: HttpRequest, username: str):
        context = {
            'username': username,
            'phones': ['483920840923', '423453253', '4532543254']
        }
        return render(request=request, template_name='home.html', context=context)