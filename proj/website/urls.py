from django.urls import path
from django.contrib import admin

from . import views
# app_name ="website"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/addarticle/', views.addarticle, name='addarticle'),
    path('dashboard/articles/article/<int:id>', views.detail, name='detail'),
    path('dashboard/articles/updata/<int:id>', views.updataArticle, name='updata'),
    path('dashboard/articles/delete/<int:id>', views.deleteArticle, name='delete'),
    path('articles/', views.articles, name='articles'),
    path('dashboard/articles/article/comment/<int:id>', views.addComment, name="comment"),


    # path('dashboard/', views.dashboard, name="dashboard"),
    # path('addarticle/', views.addarticle, name="addarticle"),
    # path('article/<int:id>/', views.detail, name="detail"),
    # path('updata/<int:id>/', views.updataArticle, name="updata"),
    # path('delete/<int:id>/', views.deleteArticle, name="delete"),
    # path('', views.articles, name="articles"),
    # #path('comment/<int:id>', views.addComment, name="comment"),

]