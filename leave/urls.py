from django.urls import path
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

]

