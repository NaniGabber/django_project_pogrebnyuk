"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path("", include(tf_urls)),
    path("donttouchmethere/", admin.site.urls),

    path("bazar/", include("bazar.urls")),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
    # path(
    #     "login/",
    #     auth_views.LoginView.as_view(
    #         template_name="accounts/login.html",
    #         redirect_authenticated_user=True,
    #         next_page="profile",
    #     ),
    #     name="login",
    # ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("api/", include("api.urls")),
    # Token auth
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
