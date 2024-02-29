from django import forms
from django.contrib.auth import get_user_model

from web.models import News, NewsTag, Comment, Settings, Profile

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class NewsForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = News
        fields = ('title', 'tags', 'text')


class NewsTagForm(forms.ModelForm):
    class Meta:
        model = NewsTag
        fields = ('title', )


class NewsFilterForm(forms.Form):
    search = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"placeholder": "Поиск"}),
        required=False
    )

    sort = forms.ChoiceField(
        label='Сортировать по',
        choices=[
            ('post_date', 'дате'),
            ('title', 'названию'),
            ('user', 'автору'),
            ('comment_count', 'кол-ву комментариев'),
            ('favorite_count', 'кол-ву добю. в изб.')
        ]
    )


class CommentsForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        self.instance.news = self.initial['news']
        return super().save(commit)

    class Meta:
        model = Comment
        fields = ('text', )


class RegistrationFormForAdmin(RegistrationForm):
    is_admin = forms.ChoiceField(
        label='Добавить в админку?',
        widget=forms.CheckboxInput,
        required=False
    )


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('color', 'font_size', 'font_color')


class BlockedUser(forms.Form):
    account = forms.ChoiceField(
        choices=[(i.id, i.username) for i in User.objects.all()]
    )
    time_unblock = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        )
    )