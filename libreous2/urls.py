"""libreous2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import main.views as alo
import Auth.views as auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', alo.emp),
    path('register', auth.signup),
    path('login', auth.log_in),
    path('logout', auth.logout_request, name="logout"),
    path('search/', alo.go_search, name='search_result'),
    path('book/<int:pk>/', alo.book_detail, name='post-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
