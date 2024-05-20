# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('upload_data/', views.upload_data, name='upload_data'),
    path('success/', views.success, name='success'),
    path('query_builder/', views.query_builder, name='query_builder'),
    path('users/', views.users, name='users'),
    path('add_user', views.add_user, name='add_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('query/success/', views.query_success, name='query_success'),
    path('logout/', views.logout_view, name='logout'),

]
