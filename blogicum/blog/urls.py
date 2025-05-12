from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.create_post, name='create_post'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
    path('profile/<str:profile_username>/',
         views.user_profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
