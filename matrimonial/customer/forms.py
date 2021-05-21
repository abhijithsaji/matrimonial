from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.models import fields_for_model
from. models import *



class LoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name','address','city','country','date_of_birth','phone','gender','phone']

class CustomerBasicForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['age','height','weight','martial_status','mother_tongue','physical_status',
		'about_me','education','specification','school_name','school_location',
		'year_of_passout_school','college_name_ug',
		'college_location_ug','course_ug','year_of_passout_college_ug',
		'college_name_pg','college_location_pg','course_pg','year_of_passout_college_pg',
		'company_name','designation','company_location','lan_number','phone']

class CustomerPersonalForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['complexion','body_type','blood_group','occupation','employed_in','annual_income',
					'star_sign','about_my_family','fathers_name','fathers_family_name','fathers_ancestral_place',
					'fathers_employed_in','fathers_occupation','fathers_company_name','fathers_company_location',
					'mothers_name','mothers_family_name','mothers_ancestral_place','mothers_employed_in','mothers_occupation',
					'mothers_company_name','mothers_company_location','country_living_in','current_location','permanent_location',
					'residential_status','belongs_to']


class CustomerPersonalityForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['diet','smoking','drinking']


class CustomerAstroForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['date_of_birth','time_of_birth','place_of_birth','longtitude','latitude']



class MultiForm(forms.ModelForm): 
	
       
	movie_types = forms.ModelMultipleChoiceField(
		queryset=MovieTypes.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)

	music_types = forms.ModelMultipleChoiceField(
		queryset=MusicType.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)

	reading_types = forms.ModelMultipleChoiceField(
		queryset=ReadingType.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)
	
	sport_types = forms.ModelMultipleChoiceField(
		queryset=SprortType.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)

	
	food_types = forms.ModelMultipleChoiceField(
		queryset=FoodType.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)

	dress_types = forms.ModelMultipleChoiceField(
		queryset=DressType.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False)


	class Meta: 
			model = Customer 
			fields = []



				
	