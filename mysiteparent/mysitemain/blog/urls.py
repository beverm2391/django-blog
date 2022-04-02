from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('index', views.HomePageView.as_view() , name = 'index'),
    path('about-me/', views.AboutMePageView.as_view(), name='about-me'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]