from django.contrib import admin
from django.urls import path

from articles.views import article_list, article_detail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('articles/', article_list, name = 'list'),
    path('articles/<int:article_id>', article_detail, name = 'detail'),

]
