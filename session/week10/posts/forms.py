from django import forms
from .models import Post
# forms는 model과 비슷


class PostBasedfForm(forms.Form):
    class Meta:
        model = Post
        fields = '__all__'  # Post class의 모든 항목을 가지고 옴


class PostCreatedForm(PostBasedfForm):
    class Meta(PostBasedfForm.Meta):
        fields = ['image', 'content']


class PostUpdateForm(PostBasedfForm):
    class Meta(PostBasedfForm.Meta):
        fields = ['image', 'content']


class PostDetailForm(PostBasedfForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['disabled'] = True
