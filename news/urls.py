from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # other URL patterns here
    path('news/<int:article_id>/', views.news_detail, name='news_detail'),
]