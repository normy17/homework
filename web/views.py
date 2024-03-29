from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import Group

from web.forms import *
from web.models import *
from web.services import filter_news, filter_comment


@login_required
def main_view(request):
    news = News.objects.all()
    admin = False

    if request.user.groups.filter(name='admins'):
        admin = True

    filter_form = NewsFilterForm(request.GET)
    filter_form.is_valid()
    news = filter_news(news, filter_form.cleaned_data)

    total_count = news.count()
    page_number = request.GET.get("page", 1)
    paginator = Paginator(news, per_page=3)

    return render(request, "web/main.html", {
        'news': paginator.get_page(page_number),
        'total_count': total_count,
        'filter_form': filter_form,
        'admin': admin
    })


def news_edit_view(request, id=None):
    news = get_object_or_404(News, id=id) if id is not None else None
    form = NewsForm(instance=news)
    if request.method == 'POST':
        form = NewsForm(data=request.POST, instance=news, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "web/news_create.html", {
        "form": form
    })


def news_delete_view(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('main')


def news_view(request, id):
    news = get_object_or_404(News, id=id)
    admin = False
    if request.user.groups.filter(name='admins'):
        admin = True
    comments = Comment.objects.all()
    comments = filter_comment(comments, news)
    form = CommentsForm()
    if request.method == 'POST':
        form = CommentsForm(data=request.POST, initial={"user": request.user, "news": news})
        if form.is_valid():
            form.save()
            news.comment_count += 1
            news.save()
            return redirect("news", id)
    return render(request, "web/current_news.html", {
        "news": news,
        "form": form,
        "comments": comments,
        "admin": admin
    })


def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('main')


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )

            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = Profile(account=user)
            profile.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form,
        "is_success": is_success
    })


def reg_user_for_admin(request):
    form = RegistrationFormForAdmin()
    users = User.objects.all()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )

            user.set_password(form.cleaned_data['password'])
            user.save()
            if 'is_admin' in request.POST and request.POST['is_admin'] == 'on':
                user.groups.add(Group.objects.get(name='admins'))
            user.save()
            profile = Profile(account=user)
            profile.save()
            return redirect('reg_user_for_admin')
    return render(request, 'web/reg_for_admin.html', context={
        'form': form,
        'users': users
    })


def block_user(request):
    form = BlockedUser()
    if request.method == 'POST':
        form = BlockedUser(data=request.POST)
        if form.is_valid():
            user = get_object_or_404(User, id=form.cleaned_data['account'])
            user.profile.is_blocked = True
            user.profile.time_unblock = form.cleaned_data['time_unblock']
            user.profile.save()
    return render(request, 'web/block_user.html', context={
        'form': form
    })


def user_delete_view(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('reg_user_for_admin')


def settings(request):
    instance = Settings.objects.first()
    form = SettingsForm(instance=instance)
    if request.method == "POST":
        setting = Settings.objects.first()
        form = SettingsForm(data=request.POST, instance=setting)
        if form.is_valid():
            form.save()

            return redirect('settings')
    return render(request, 'web/settings.html', context={
        'form': form
    })


# def auth_view(request):
#     form = AuthForm()
#     if request.method == 'POST':
#         form = AuthForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(**form.cleaned_data)
#             if user is None:
#                 form.add_error(None, "Неправильный логин или пароль")
#             else:
#                 if user.profile.is_blocked == True and user.profile.time_unblock >= timezone.now():
#                     return HttpResponse('Вы заблокированы!')
#                 else:
#                     user.profile.is_blocked = False
#                     user.profile.save()
#                     login(request, user)
#                     return redirect("main")
#     return render(request, 'web/auth.html', {
#         "form": form
#     })
def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Неправильный логин или пароль")
            else:
                if user.profile.is_blocked == True and user.profile.time_unblock > timezone.now():
                    return HttpResponse('Вы заблокированы')
                else:
                    user.profile.is_blocked = False
                    user.profile.save()
                    login(request, user)
                    return redirect("main")
    return render(request, 'web/auth.html', {
        "form": form
    })

def logout_view(request):
    logout(request)
    return redirect("main")


def tags_view(request):
    tags = NewsTag.objects.all()
    form = NewsTagForm()
    if request.method == 'POST':
        form = NewsTagForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags')
    return render(request, 'web/tags.html', {
        'tags': tags,
        'form': form
    })


def tags_delete_view(request, id):
    tags = get_object_or_404(NewsTag, id=id)
    tags.delete()
    return redirect('tags')


def favorite_add_view(request, id):
    user = request.user
    news = get_object_or_404(News, id=id)

    favorite, created = Favorite.objects.get_or_create(user=user, news=news)

    if not created:
        favorite.delete()
        news.favorite_count -= 1
        news.save()
    else:
        news.favorite_count += 1
        news.save()

    return redirect('favorites')


def favorite_view(request):
    user = request.user
    news = Favorite.objects.filter(user=user)

    return render(request, 'web/favorites.html', {
        'news': news
    })
