from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup),
    path('welcome', views.welcome),
    path('logout', views.logout_page),
    path('changeinfo', views.changeInfo),
    path('changeinfo/<id>/', views.verify_page),
    path('deleteaccount', views.delete_account),
    path('signup/<id>/', views.verify_page),
    path('forgotpassword', views.forgot_my_password_start),
    path('forgotpassword/<id>/', views.forgot_my_password_end),
    path('setemail', views.setEmail_start),
    path('setemail/<id>/', views.setEmail_end),
]