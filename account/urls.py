from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('signup-view/', views.signup, name='signup'),
    path('password-change-view/', views.password_change, name='password_change'),

    # built-in django auth views
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/confirm/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    # url("^password-reset-confirm/(?P<uidb64>[^/]+)/token>/$']$/", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
