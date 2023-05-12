from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


# user Registration 
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		# self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		# self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		# self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone number", "class":"form-control"}), label="")
	date_of_birth  = forms.CharField(required=True, widget=forms.widgets.DateTimeInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}), label="")
	location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location / City", "class":"form-control"}), label="")
	gender =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Male / Female", "class":"form-control"}), label="")
	marital_status =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Single, Engaged or Married ", "class":"form-control"}), label="")
	life_connect =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Life Connect", "class":"form-control"}), label="")
	department =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Department", "class":"form-control"}), label="")
	place_of_work =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Place of Work or School", "class":"form-control"}), label="")
	specific_life_objective = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Specific Life Objective", "class":"form-control"}), label="")
	class Meta:
		model = Record
		exclude = ("user",)
  