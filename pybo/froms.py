from django import forms
from pybo.models import Answer, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows': 10}),
        # }
        lables = {
            'subject': '제목',
            'content': '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        lables = {
            'content': '답변 내용'
        }