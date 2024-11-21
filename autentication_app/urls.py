from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_view, name='login' ),
    path('registrar/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('users/delete/<int:user_id>/', views.delete_user, name='user_delete'),
    path('users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)