# forms.py


from django import forms
from .models import Job, Feedback


class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'company_image', 'position', 'salary', 'deadline', 'required_skills', 'location', 'description']

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control'}),
            'required_skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'enrollment_no', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' }),
            'enrollment_no': forms.TextInput(attrs={'class': 'form-control' }),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
