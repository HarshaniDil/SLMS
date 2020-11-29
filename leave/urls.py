from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',views.loginpage, name="login"),
    path('register/', views.registerpage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('apply2/<str:pk>/', views.apply2,name="apply2"),
    path('', views.home,name="home-page"),
    path('head/', views.head),
    path('employee/<str:pk_test>/', views.employee1,name="Head_Side_Emp_View"),
    path('leaves/', views.leaves,name="leaves"),
    path('update/<str:pk>/', views.updateStatus, name="updateStatus"),
    path('user/', views.user_page, name="user-page"),
    path('Profile/', views.accountSettings, name="account"),  
    path('res_leaves/', views.res_leaves, name="res_leaves"),   

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="home/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_form.html"), 
    name="password_reset_confirm"),
    
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_done.html"), 
    name="password_reset_complete"),

]

