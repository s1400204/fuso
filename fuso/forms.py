from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        # forms.py

# プルダウンの選択肢
CHOICES = (
    ("request.POSTの中身", "画面に表示される内容")
    ("0", "項目1")
    ("1", "項目2")
    ("2", "項目3")
    ("3", "項目4")
)
class InputForm(forms.Form):
    """定数リストによるプルダウンメニュー"""
    pulldown = forms.ChoiceField(widget=forms.Select, 
                                 choices=CHOICES, # 定数リストを指定する
                                 label="ラベル名")