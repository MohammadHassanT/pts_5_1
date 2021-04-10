from django.shortcuts import render, HttpResponse 


def home_page_view(request):
    return HttpResponse('<h2> This is the home page </h2>')


def about_page_view(request):
    return HttpResponse('<h2> This is the aobut page </h2>')

