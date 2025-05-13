from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Category, Comment, Post, User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm, UserForm
from django.core.paginator import Paginator
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
DeleteView, DetailView, ListView, UpdateView)


def post_pagination(post_list, obj_count, request):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def comment_count():
    pass



def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ).order_by('-pub_date')
    
    page_obj = post_pagination(post_list, 10, request)

    context = {'page_obj': page_obj}
    return render(request, template, context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()

    return redirect('blog:post_detail', pk=post_id)

'''
def post_detail(request, post_id):
    template = 'blog/detail.html'

    post = get_object_or_404(Post, pk=post_id)

    form = CommentForm(request.POST or None)

    comments = Comment.objects.order_by('-created_at')
    context = {'post': post, 'form': form, 'comments' : comments}
    if form.is_valid():
        form.save()
    context.update({'form': form})
    return render(request, template, context) '''


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comments.count'] = post_comments(self.object.comments)
        # Записываем в переменную form пустой объект формы.
        context['form'] = CommentForm()
        # Запрашиваем все поздравления для выбранного дня рождения.
        context['comments'] = self.object.comment.select_related('author')
        return context 




def post_delete(request, post_id):
    template = 'blog/detail.html'
    redirection = 'blog/index.html'

    instance = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    context = {'form' : form, 'post' : instance}

    if request.method == 'POST':
        instance.delete()
        return reverse_lazy('blog:index')
    return render(request, template, context)



def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects, slug=category_slug,
        is_published=True, created_at__lte=datetime.now()
    )
    post_list = Post.objects.filter(
        is_published=True,
        category__slug=category_slug,
        pub_date__lte=datetime.now()
    )

    page_obj = post_pagination(post_list, 10, request)

    context = {'page_obj': page_obj, 'category': category}
    return render(request, template, context)
 


def create_post(request, post_id=None):
    template = 'blog/create.html'
    
    if post_id is not None: instance = get_object_or_404(Post, pk=post_id)
    else: instance = None

    form = PostForm(request.POST or None, instance=instance,
                    files=request.FILES or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        context.update({'form': form})
    return render(request, template, context)



def user_profile(request, profile_username):
    template = 'blog/profile.html'
    profile = get_object_or_404(
        User.objects, username=profile_username,
    )
    pages = Post.objects.filter(
        author__username = profile_username
    )

    page_obj = post_pagination(pages, 10, request)
    
    context = {'profile': profile, 'page_obj': page_obj}
    return render(request, template, context) 


def single_comment(request, post_id=None, comment_id=None):
    template = 'blog/comment.html'
    if id is not None: instance = get_object_or_404(Post, pk=id)
    else: instance = None
    context = {'form' : form}
    form = Comment(request.POST or None, instance=instance)
    if form.is_valid():
        context.update({'form' : form})
        form.save()
    return render(request, template, context)


def registration(request):
    template = 'registration/registration_form.html'
    form = UserForm(request.POST or None, instance=None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, template, context)
