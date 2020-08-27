from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import apply
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import django_filters
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
 

class ExampleForm(forms.Form):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    date = forms.DateField(widget=DateInput)
     
class ExampleTimeForm(forms.Form):
    from_time = forms.TimeField(widget=TimeInput)
    to_time = forms.TimeField(widget=TimeInput)
     
#update form in HoD side
class ApplyForm(forms.ModelForm):
    
    class Meta:

        model = apply
        fields = ('employee','leave','from_date','date','to_date','from_time','to_time','reason','status')
        widgets = {'date':DateInput(),'from_date': DateInput(),'to_date': DateInput(),'from_time': TimeInput(),'to_time': TimeInput(),'reason': forms.Textarea(attrs={'rows':4, 'cols':15})
        }

        
    def __init__(self,*args, **kwargs):
        super(ApplyForm,self).__init__(*args, **kwargs)
        self.fields['leave'].empty_label = "select"

# apply form       
class ApplyForm1(forms.ModelForm):
    
    class Meta:

        model = apply
        fields = ('employee','leave','from_date','date','to_date','from_time','to_time','reason','status')
        widgets = {'date':DateInput(),'from_date': DateInput(),'to_date': DateInput(),'from_time': TimeInput(),'to_time': TimeInput(),'reason': forms.Textarea(attrs={'rows':4, 'cols':15})
        }
  
    def __init__(self,*args, **kwargs):
        super(ApplyForm1,self).__init__(*args, **kwargs)
        self.fields['leave'].empty_label = "select"
        self.fields['employee'].widget = forms.widgets.HiddenInput()
        self.fields['status'].widget = forms.widgets.HiddenInput()


class CommentForm(forms.ModelForm):
    
    class Meta:

        model = comment
        fields = '__all__'
      
    def __init__(self,*args, **kwargs):
        super(CommentForm,self).__init__(*args, **kwargs)
      
      
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class EmployeeForm(ModelForm):
        
    class Meta:
        model = employee
        fields = '__all__'
        exclude = ['user','leave']


    