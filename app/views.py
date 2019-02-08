from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



def home(request):
    context = {
    "posts":Post.objects.all()
    }
    return render(request,'blog/home.html',context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'  # <app>/<model>_<viewtype>.html

# class PostCreateView(LoginRequiredMixin, CreateView):
class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'  # <app>/<model>_<viewtype>.html


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
