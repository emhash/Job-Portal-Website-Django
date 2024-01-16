from django.shortcuts import render,redirect,get_list_or_404


def index(request):

    return render(request, "home/pages/index.html")