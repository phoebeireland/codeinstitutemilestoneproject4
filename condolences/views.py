from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

def view_condolences(request):
    """ A view that renders the bag contents page """

    return render(request, 'condolences/condolences.html')