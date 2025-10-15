from django import forms
from .models import Blog

# Add blog form

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description", "content", 'author']

