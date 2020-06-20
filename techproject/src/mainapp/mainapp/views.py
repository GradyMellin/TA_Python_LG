from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["one","two","three","four"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)
