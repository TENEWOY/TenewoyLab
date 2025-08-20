from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('it2025/', views.it2025, name='it2025'),
    path('contacts/', views.contacts, name='contacts'),
    path('worker/', views.worker, name='worker'),
    path('courses/', views.courses, name='courses'),
    path('news/', views.news, name='news'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('money/', views.money, name='money'),
    path("stats/", views.stats, name="stats"),
]
