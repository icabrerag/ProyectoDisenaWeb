"""diseñaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 

from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, logout_then_login

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^plan/',include('apps.plan.urls')),
    url(r'^compra/',include('apps.compra.urls')),
    url(r'^usuario/',include('apps.usuario.urls')),
    url(r'accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    url('logout/', logout_then_login, name="logout"),
    url('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    url('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    url('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
    
   
    
    
]
