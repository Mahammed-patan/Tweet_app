from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('tweet/', views.create_tweet, name='create_tweet'),
    path('category_tweet/<str:data>', views.Category_tweet, name='tweet_data'),
]