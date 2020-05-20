from django import forms

from .models import MySkills

class MySkillsForm(forms.ModelForm):

    class Meta:
        model = MySkills
        fields = ('title', 'icon_class', 'description', 'skills')