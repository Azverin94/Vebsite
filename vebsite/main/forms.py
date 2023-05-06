from .models import Task
from django.forms import ModelForm,widgets,TextInput

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task","comment"]
        widgets={"title":TextInput(attrs={'class':'form-control','placeholder':'Введите название'}),
                 "task":TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
        "comment": TextInput(attrs={'class': 'form-control', 'placeholder': 'Комментарий'})}
