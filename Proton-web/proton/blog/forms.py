from django import forms
from django.forms import ModelForm
from .models import Post

CATEGORIES = (
    ('html', 'Html'),
    ('css', 'Css'),
    ('javascript', 'Javascript'),
    ('python', 'Python')
)

class CreatePostForm(ModelForm):
    # category = forms.ChoiceField(choices=CATEGORIES,widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'image')

        labels = {
            'title': '',
            'body': '',
            'category': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            #'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
        }