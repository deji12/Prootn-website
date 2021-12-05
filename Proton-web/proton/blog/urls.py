from django.urls import path
from .views import BlogHome, Login, Register, AdminPage, LogoutAdmin, Article, CreatePost, ArticleDetailView

urlpatterns = [
    path('blog-home/', BlogHome, name="blog-home"),
    path('dashboard-login/', Login, name="dashboard-login"),
    path('register-dashboard/', Register, name="register-dashboard"),
    path('dashboard/', AdminPage, name="dashboard"),
    path('logout/', LogoutAdmin, name="logout"),
    #path('<int:id>/', Article, name="article-page"),
    path('create-post/', CreatePost, name="create-post"),
    path('<int:id>/', ArticleDetailView.as_view(), name="article-page"),
]