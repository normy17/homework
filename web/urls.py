from django.urls import path

from web.views import *

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("news/add/", news_edit_view, name="news_add"),
    path("news/<int:id>/", news_edit_view, name="news_edit"),
    path("news/<int:id>/delete/", news_delete_view, name="news_delete"),
    path('tags/', tags_view, name='tags'),
    path('tags/<int:id>/delete/', tags_delete_view, name='tags_delete'),
]