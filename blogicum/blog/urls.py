from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import *

app_name = 'blog'
template_str = 'registration/'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/comment', views.add_comment, name='add_comment'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.create_post, name='create_post'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
    path('profile/<str:profile_username>/',
         views.user_profile, name='profile'),
    path('auth/registration/',
         views.registration, name='registration'),

    path('auth/login/',
         LoginView.as_view(template_name=template_str+'login.html'),
         name='login'),
    path('auth/logout/',
         LogoutView.as_view(template_name=template_str+'logged_out.html'),
         name='logout'),
    path('auth/password_change_done/',
         PasswordChangeDoneView.as_view(template_name=template_str+'password_change_done.html'),
         name='password_change_done'),
    path('auth/password_change_form/',
         PasswordChangeView.as_view(template_name=template_str+'password_change_form.html'),
         name='password_change_form'),
    path('auth/password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name=template_str+'password_reset_complete.html'),
         name='password_reset_complete'),
    path('auth/password_reset_confirm/',
         PasswordResetConfirmView.as_view(template_name=template_str+'password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('auth/password_reset_done/',
         PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('auth/password_reset_form/',
         PasswordResetView.as_view(template_name=template_str+'password_reset_form.html'),
         name='password_reset_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
