from django.shortcuts import render

def view_about(request):
    """ A view that renders the about page """

    return render(request, 'about/about.html')