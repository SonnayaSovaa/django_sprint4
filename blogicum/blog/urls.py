from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

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

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
path('auth/login/',
         views.login, name='login'),
    path('auth/logout/',
         views.logout, name='logout'),
    path('auth/password_change_done/',
         views.password_change_done, name='password_change_done'),
    path('auth/password_change_form/',
         views.password_change_form, name='password_change_form'),
    path('auth/password_reset_complete/',
         views.password_reset_complete, name='password_reset_complete'),
    path('auth/password_reset_confirm/',
         views.password_reset_confirm, name='password_reset_confirm'),
    path('auth/password_reset_done/',
         views.password_reset_done, name='password_reset_done'),
    path('auth/password_reset_form/',
         views.password_reset_form, name='password_reset_form'),

     '''