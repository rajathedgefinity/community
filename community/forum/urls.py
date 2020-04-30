from django.urls import path
from . import views

urlpatterns = [
    path('dash/',views.home,name='dash'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup_user,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('user_account/',views.user_account,name='user_account'),
    path('user_thread_comments/',views.user_thread_comments,name='user_thread_comments'),
]
