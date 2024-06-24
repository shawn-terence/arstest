"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from api.views import*

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("assets/add/", AssetAddView.as_view(), name="asset_add"),
    path("user/update-password/", UserUpdatePasswordView.as_view(), name="user_update_password"),
    path("user/change-role/", ChangeUserRoleView.as_view(), name="user_change_role"),
    path("user/delete/", DeleteUserView.as_view(), name="user_delete"),
    path("users/", AllUsersView.as_view(), name="user_list"),
    path("assets/", AssetListView.as_view(), name="asset_list"),
    path("assets/<int:asset_id>/request/", AssetUpdateView.as_view(), name="asset_request"),
    path("requests/", RequestListView.as_view(), name="request_list"),
    path("requests/<int:request_id>/action/", RequestActionView.as_view(), name="request_action"),
    path("user/details/", UserDetailView.as_view(), name="user_details"),
    path("requests/<int:request_id>/delete/", UserRequestDeleteView.as_view(), name="user_request_delete"),  
]
