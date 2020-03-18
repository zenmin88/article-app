from django.shortcuts import redirect, Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .models import Article
from users.models import CustomUser


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    # success_url = reverse_lazy('article_list')
    fields = ['title', 'body']
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleByAuthorList(ListView):
    model = Article
    template_name = 'article_list.html'

    def get_queryset(self):
        user = CustomUser.objects.get(username=self.kwargs['author'])
        print(self.kwargs['author'], user)
        return Article.objects.filter(author=user)



