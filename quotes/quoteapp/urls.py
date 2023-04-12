from django.contrib import admin
from . import views
from django.urls import path, include


app_name = 'quoteapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('authors/', views.add_author, name='author'),
    path('quotes/', views.add_quote, name='quote'),
    path('tags/', views.add_tag, name='tag'),
    path("info/", views.info, name="info"),
    path("info/detail_author/<int:author_id>", views.author_page, name='detail_author'),
    path("info/detail_quotes/<int:quote_id>", views.author_page, name='detail_quotes')

]