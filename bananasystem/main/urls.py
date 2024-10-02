from django.urls import path
from main import views
from django.contrib.auth import views as auth_views
# from bananasystem import settings
from django.conf import settings
from django.conf.urls.static import static

#main views
urlpatterns = [
    path("index/", views.index, name="index"),
]

#auth
urlpatterns += [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name = "logout"),
    path("register/", views.register, name="register"),

]

#password reset
urlpatterns += [
    path("password_reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

#password change
urlpatterns += [
    path("password_change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

#profile
urlpatterns += [
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/update/", views.edit_profile, name="edit_profile"),
]
