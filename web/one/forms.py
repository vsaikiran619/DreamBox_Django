from django import forms
from .models import Categoryposts,Comment,Interview


class CommentForm(forms.ModelForm):
    comment = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'usercomment',
        'rows':'4'
    }))
    class Meta:
        model = Comment
        fields = ('comment',)

class InterviewForm(forms.ModelForm):
    company_name = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'company_name',
        'rows':'1',
        'placeholder':'Enter the company name'
    }))
    name = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'name',
        'rows':'1',
        'placeholder':'Enter Your name'
    }))
    selected_year = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'selected_year',
        'rows':'1',
        'placeholder':'Enter Selected Year'
    }))
    package = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'package',
        'rows':'1',
        'placeholder':'Enter The package offered'
    }))
    role = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'role',
        'rows':'1',
        'placeholder':'Enter Your selected role'
    }))
    qualification = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'qualification',
        'rows':'1',
        'placeholder':'Enter your qualification'
    }))
    skills = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'skills',
        'rows':'4',
        'placeholder':'Enter required skills'
    }))
    rounds = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'rounds',
        'rows':'1',
        'placeholder':'Enter The no.of rounds'
    }))
    interview_Experience = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'interview_Experience',
        'rows':'6',
        'placeholder':'Please explain each round'
    }))
    questions = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'questions',
        'rows':'6',
        'placeholder':'Please Enter the questions faced in the interview'
    }))
    suggestions = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'suggestions',
        'rows':'4',
        'placeholder':'Please give me any suggestions for interview(if possible)'
    }))
    class Meta:
        model = Interview
        fields = (
            'company_name',
            'name',
            'selected_year',
            'package',
            'role',
            'qualification',
            'skills',
            'rounds',
            'interview_Experience',
            'questions',
            'suggestions'
            )


