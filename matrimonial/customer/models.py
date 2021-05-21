from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from .validators import validate_num




class Religion(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Caste(models.Model): 

    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Nakshatra(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class MusicType(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class ReadingType(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class MovieTypes(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class SprortType(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class FoodType(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class DressType(models.Model): 
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model): 
    # Registration

    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, choices = [('Male','male'),('Female','female'),('Other','other')],null=True)
    address = models.TextField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=13, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)
    uname = models.CharField(max_length=200,null=True)

    image = models.ImageField(upload_to='static/images/profile',default='static/images/user.png')

    # Basic information

    age = models.PositiveIntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    martial_status = models.CharField(max_length=20, choices = [('Unmarried','unmarried'),('Divorced','divorced'),
        ('Separated','separated'),('Widow/Widower','widow/widower')],null=True)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE,null=True,blank=True)
    caste = models.ForeignKey(Caste, on_delete=models.CASCADE,null=True,blank=True)
    mother_tongue = models.CharField(max_length=20, choices = [('Malayalam','malayalam'),('Hindi','hindi'),('Tamil','Tamil'),
        ('English','english'),('Other','other')],null=True,blank=True)
    physical_status = models.CharField(max_length=20, choices = [('Healthy','healthy'),('Mild','mild'),('Rather Not To Say','rather not to say')],null=True,blank=True)
    about_me = models.TextField(max_length = 1000,null=True)

    education = models.CharField(max_length=50,null=True)
    specification = models.CharField(max_length=50,null=True)

    school_name = models.CharField(max_length=50,null=True,blank=True)
    school_location = models.CharField(max_length=50,null=True,blank=True)
    year_of_passout_school = models.PositiveIntegerField(null=True,blank=True)

    college_name_ug = models.CharField(max_length=50,null=True,blank=True)
    college_location_ug = models.CharField(max_length=50,null=True,blank=True)
    course_ug = models.CharField(max_length=50,null=True,blank=True)
    year_of_passout_college_ug = models.PositiveIntegerField(null=True,blank=True)

    college_name_pg = models.CharField(max_length=50,null=True,blank=True)
    college_location_pg = models.CharField(max_length=50,null=True,blank=True)
    course_pg = models.CharField(max_length=50,null=True,blank=True)
    year_of_passout_college_pg = models.PositiveIntegerField(null=True,blank=True)

    company_name = models.CharField(max_length=50,null=True,blank=True)
    designation = models.CharField(max_length=50,null=True,blank=True)
    company_location = models.CharField(max_length=50,null=True,blank=True)

    lan_number = models.CharField(max_length=13, null=True)


    # Personal Information

    complexion = models.CharField(max_length=20, choices = [('fair','Fair'),('whiteatish','Whiteatish'),('dark','Dark')],null=True,blank=True)
    body_type = models.CharField(max_length=20, choices = [('normal','Normal'),('Athletic','athletic'),('Other','other')],null=True,blank=True)
    blood_group = models.CharField(max_length=20, choices = [('A +','A +'),('B +','B +'),('A -','A -'),
                                                ('B -','B -'),('AB -','AB -'),('AB +','AB +'),('O +','O -'),
                                                ('O -','O -'),('other','Other')],null=True,blank=True)
    occupation = models.CharField(max_length=50,null=True)
    employed_in = models.CharField(max_length=50,null=True)
    annual_income = models.PositiveIntegerField(null=True)
    star_sign = models.ForeignKey(Nakshatra, on_delete=models.CASCADE,null=True)
    about_my_family = models.TextField(max_length=1000,null=True,blank=True)

    fathers_name = models.CharField(max_length=50,null=True)
    fathers_family_name = models.CharField(max_length=50,null=True)
    fathers_ancestral_place = models.CharField(max_length=50,null=True)
    fathers_employed_in = models.CharField(max_length=50,null=True,blank=True)
    fathers_occupation = models.CharField(max_length=50,null=True)
    fathers_company_name = models.CharField(max_length=50,null=True,blank=True)
    fathers_company_location = models.CharField(max_length=50,null=True,blank=True)

    mothers_name = models.CharField(max_length=50,null=True)
    mothers_family_name = models.CharField(max_length=50,null=True)
    mothers_ancestral_place = models.CharField(max_length=50,null=True)
    mothers_employed_in = models.CharField(max_length=50,null=True,blank=True)
    mothers_occupation = models.CharField(max_length=50,null=True)
    mothers_company_name = models.CharField(max_length=50,null=True,blank=True)
    mothers_company_location = models.CharField(max_length=50,null=True,blank=True)

    country_living_in = models.CharField(max_length=50,null=True)
    current_location = models.CharField(max_length=50,null=True)
    permanent_location = models.CharField(max_length=50,null=True)
    residential_status = models.CharField(max_length=20, choices = [('own','Own'),('rented','Rented'),('other','Other')],null=True)
    belongs_to = models.CharField(max_length=50,null=True, blank=True)

    # My personality

    diet = models.CharField(max_length=20, choices = [('any','Any'),('vegitarian','Vegiterian'),('eggetarian','Eggetarian'),('nonvegiterian','NonVegiterian')],null=True,default='any')
    smoking = models.CharField(max_length=20, choices = [('yes','Yes'),('no','No')],null=True, blank=True)
    drinking = models.CharField(max_length=20, choices = [('yes','Yes'),('no','No'),('special functions','Special Functions only')],null=True, blank=True)
    gardening = models.PositiveIntegerField(validators=[validate_num],null=True)
    astronamy = models.PositiveIntegerField(null=True)

    music = models.PositiveIntegerField(validators=[validate_num],null=True)
    music_types = models.ManyToManyField(MusicType)

    movie = models.PositiveIntegerField(validators=[validate_num],null=True)
    movie_types = models.ManyToManyField(MovieTypes)

    reading = models.PositiveIntegerField(validators=[validate_num],null=True)
    reading_types = models.ManyToManyField(ReadingType)

    sports = models.PositiveIntegerField(validators=[validate_num],null=True)
    sport_types = models.ManyToManyField(SprortType)

    foods = models.PositiveIntegerField(validators=[validate_num],null=True)
    food_type = models.ManyToManyField(FoodType)

    dress = models.PositiveIntegerField(validators=[validate_num],null=True)
    dress_types = models.ManyToManyField(DressType)

    # Astrology information

    time_of_birth = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    place_of_birth = models.CharField(max_length=50,null=True, blank=True)
    longtitude = models.CharField(max_length=50,null=True, blank=True)
    latitude = models.CharField(max_length=50,null=True, blank=True)





    

    def __str__(self):
        return self.name