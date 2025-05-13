from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Category, Post, User
from .forms import PostForm
from django.core.paginator import Paginator
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ).order_by('-pub_date')[0:5]
    
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    if id is not None: instance = get_object_or_404(Post, pk=id)
    else: instance = None

    form = PostForm(request.POST or None, instance=instance,
                    files=request.FILES or None)
    context = {'form': form}
    if form.is_valid():
        
        context.update({'form': form})
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

    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'category': category}
    return render(request, template, context)


def user_profile(request, profile_username):
    template = 'blog/profile.html'
    profile = get_object_or_404(
        User.objects, username=profile_username,
    )
    pages = Post.objects.filter(
        author__username = profile_username
    )

    paginator = Paginator(pages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'profile': profile, 'page_obj': page_obj}
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


def user_edit_profile(request, profile_username):
    template = 'blog/profile.html'
    profile = get_object_or_404(
        User.objects, username=profile_username,
    )
    pages = Post.objects.filter(
        author__username = profile_username
    )

    paginator = Paginator(pages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'profile': profile, 'page_obj': page_obj}
    return render(request, template, context)  


def add_comment(request, post_id=None):
    template = 'blog/comment.html'
    if post_id is not None: instance = get_object_or_404(Post, pk=post_id)
    else: instance = None
    form = PostForm(request.POST or None, instance=instance,
                    files=request.FILES or None)
    context = {'comment': form}
    if form.is_valid():
        form.save()
    context.update({'comment': form})
    return render(request, template, context)


def registration(request):
    template = 'registration/registration_form.html'
    instance = None
    form = PostForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    context.update({'form': form})
    return render(request, template, context)

'''

def login(request):
    template = 'registration/login.html'
    return render(request, template)
    

def logout(request):
    template = 'registration/logged_out.html'
    return render(request, template)
    

def password_change_done(request):
    template = 'registration/password_change_done.html'
    return render(request, template)
    

def password_change_form(request):
    template = 'registration/password_change_form.html'
    return render(request, template)
    

def password_reset_complete(request):
    template = 'registration/password_reset_complete.html'
    return render(request, template)


def password_reset_confirm(request):
    template = 'registration/password_reset_confirm.html'
    return render(request, template)
    

def password_reset_done(request):
    template = 'registration/password_reset_done.html'
    return render(request, template)
    

def password_reset_form(request):
    template = 'registration/password_reset_form.html'
    return render(request, template)
'''