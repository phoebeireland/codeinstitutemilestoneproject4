from django.views import generic
from .models import Post
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def view_condolences(request):
    """ A view that renders the bag contents page """

    return render(request, 'condolences/condolences.html')