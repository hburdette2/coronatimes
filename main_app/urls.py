from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogposts/', views.blogposts_index, name='index'),
    path('blogposts/create/', views.BlogpostCreate.as_view(), name='blogposts_create'),
    path('blogposts/<int:blogpost_id>/', views.blogposts_detail, name='detail'),
    path('blogposts/<int:pk>/update/', views.BlogpostUpdate.as_view(), name='blogposts_update'),
    path('blogposts/<int:pk>/delete/', views.BlogpostDelete.as_view(), name='blogposts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
