from django import forms                                                           
from .models import App01

class App01Form(forms.ModelForm):

    class Meta:
        model = App01
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
            }),

            'content': forms.TextInput(attrs={
                'class': "form-control",
            }),

            'company_ID': forms.TextInput(attrs={
                'class': "form-control",
            }),
 
    
}
