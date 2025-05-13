from django.contrib import admin
from django.urls import include, path


handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('posts/', include('blog.urls')),
    path('category/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('profile/', include('blog.urls')),
    path('edit/', include('blog.urls')),
    path('auth/', include('blog.urls')),
    path('auth/', include('django.contrib.auth.urls')),   
]
