from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Category, Comment, Post, User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm, UserForm
from django.core.paginator import Paginator
from datetime import datetime
from django.views.generic import DetailView
from django.db.models import Count
from django.http import Http404


def post_pagination(post_list, obj_count, request):
    paginator = Paginator(post_list, obj_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def comment_count(post_list, criteria):
    post_list = post_list.annotate(comment_count=Count(criteria))
    return post_list


def publication_check(post_list):
    return post_list.filter(
        is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ).order_by('-pub_date')
    post_list = comment_count(post_list, 'comment__id').order_by('-pub_date')
    page_obj = post_pagination(post_list, 10, request)
    context = {'page_obj': page_obj}
    return render(request, template, context)


def create_edit_post(request, post_id=None):
    template = 'blog/create.html'
    if post_id is not None:
        instance = get_object_or_404(Post.objects, pk=post_id)
    else:
        instance = None
    form = PostForm(request.POST or None, instance=instance,
                    files=request.FILES or None)
    context = {'form': form, 'post': instance, 'user': request.user}
    if form.is_valid():
        if request.user.is_anonymous:
            return redirect('blog:login')
        if instance is not None and instance.author != request.user:
            return redirect('blog:post_detail', pk=post_id)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        context.update({'form': form})
        if post_id is None:
            return redirect('blog:profile', request.user.username)
        else:
            return redirect('blog:post_detail', pk=post_id)
    return render(request, template, context)


@login_required
def post_delete(request, post_id):
    template = 'blog/create.html'
    instance = get_object_or_404(Post, pk=post_id)
    if instance is not None and instance.author != request.user:
        return redirect('blog:login')
    form = PostForm(request.POST or None, instance=instance,
                    files=request.FILES or None)
    context = {'form': form, 'post': instance, 'user': request.user}
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect('blog:login')
        if instance is not None and instance.author != request.user:
            return redirect('blog:post_detail', pk=post_id)
        instance.delete()
        return redirect('blog:index')
    return render(request, template, context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comment.select_related('author')
        context['user'] = self.request.user
        if not (self.object.is_published):
            if self.request.user.is_anonymous:
                raise Http404('')
            if self.object.author != self.request.user:
                raise Http404('')
        return context


@login_required
def add_comment(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = get_object_or_404(Post.objects, pk=post_id)
        comment.save()
    return redirect('blog:post_detail', pk=post_id)


@login_required
def edit_comment(request, post_id, comment_id):
    template = 'blog/comment.html'
    instance = get_object_or_404(Comment.objects, pk=comment_id)
    if instance.author != request.user:
        return redirect('blog:login')
    form = CommentForm(request.POST or None, instance=instance)
    context = {'form': form, 'comment': instance, 'user': request.user}
    if form.is_valid():
        form.save()
        context.update({'form': form})
        return redirect('blog:post_detail', pk=post_id)
    return render(request, template, context)


@login_required
def delete_comment(request, post_id, comment_id):
    template = 'blog/comment.html'
    instance = get_object_or_404(Comment.objects, pk=comment_id)
    if instance is not None and instance.author != request.user:
        return redirect('blog:login')
    context = {'comment': instance, 'user': request.user}
    if request.method == 'POST':
        instance.delete()
        return redirect('blog:post_detail', pk=post_id)
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects, slug=category_slug,
        is_published=True, created_at__lte=datetime.now()
    )
    post_list = Post.objects.filter(
        category__slug=category_slug,
    )
    post_list = publication_check(post_list)
    post_list = comment_count(
        post_list, 'comment__id'
    ).order_by('-pub_date')
    page_obj = post_pagination(post_list, 10, request)
    context = {'page_obj': page_obj, 'category': category}
    return render(request, template, context)


def user_profile(request, profile_username):
    template = 'blog/profile.html'
    profile = get_object_or_404(
        User.objects, username=profile_username,
    )
    post_list = Post.objects.filter(
        author__username=profile_username
    )
    if request.user.username != profile_username:
        post_list = publication_check(post_list)
    post_list = comment_count(
        post_list, 'comment__id'
    ).order_by('-pub_date')
    page_obj = post_pagination(post_list, 10, request)

    context = {'profile': profile, 'page_obj': page_obj}
    return render(request, template, context)


@login_required
def edit_profile(request):
    template = 'blog/user.html'
    user = get_object_or_404(
        User.objects, username=request.user.username
    )
    form = UserForm(request.POST or None, instance=user)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('blog:profile', request.user.username)
    return render(request, template, context)
