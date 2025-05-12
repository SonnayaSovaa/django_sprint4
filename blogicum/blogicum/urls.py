from django.contrib import admin
from django.urls import include, path


handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

urlpatterns = [
    path('', include('blog.urls')),
    path('posts/', include('blog.urls')),
    path('category/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    
    path('auth/', include('django.contrib.auth.urls')),
]

'''
    path(
        'logout/',
        views.LogoutView.as_view(template_name='logged_out.html'),
        name='logout',
    ),
    path(
        'password_change_done/',
        views.LogoutView.as_view(template_name='password_change_done.html'),
        name='password_change_done',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(template_name='logged_out.html'),
        name='logout',
    ),
    path(
        'password_change_form/',
        views.LogoutView.as_view(template_name='password_change_form.html'),
        name='password_change_form',
    ),
    path(
        'password_reset_complete/',
        views.LogoutView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete',
    ),
    path(
        'password_reset_confirm/',
        views.LogoutView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    path(
        'password_reset_done/',
        views.LogoutView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done',
    ),
    path(
        'password_reset_form/',
        views.LogoutView.as_view(template_name='password_reset_form.html'),
        name='password_reset_form',
    ),
    path(
        'registration_form/',
        views.LogoutView.as_view(template_name='registration_form.html'),
        name='registration_form',
    ),'''