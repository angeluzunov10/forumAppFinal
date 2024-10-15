from django import forms

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        error_messages = {
            'title': {
                'required': 'Please enter a title of your post.',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters.'
            }
        }


class PostCreateForm(PostForm):
    pass


class PostEditForm(PostForm):
    pass


class PostDeleteForm(PostForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a specific post...',
            }
        )
    )