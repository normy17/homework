from django.urls import path

from web.views import *

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("news/add/", news_edit_view, name="news_add"),
    path("news/<int:id>/edit", news_edit_view, name="news_edit"),
    path("news/<int:id>/", news_view, name="news"),
    path("comments/<int:id>/delete", comment_delete, name="comment_delete"),
    path("news/<int:id>/delete/", news_delete_view, name="news_delete"),
    path('tags/', tags_view, name='tags'),
    path('tags/<int:id>/delete/', tags_delete_view, name='tags_delete'),
    path('favorites/', favorite_view, name='favorites'),
    path('favorites/<int:id>/add-delete', favorite_add_view, name='favorite_add-delete'),
    path('reg_user/', reg_user_for_admin, name='reg_user_for_admin'),
    path('reg_user/<int:id>/delete', user_delete_view, name='delete_user'),
    path('settings/', settings, name='settings'),
    path('block_user/', block_user, name='block_user')
]