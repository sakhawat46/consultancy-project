from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField
from login_app.models import User

# class Package(models.Model):
#     PACKAGE_NAME = (
#         ('Platinum', 'Platinum'),
#         ('Gold', 'Gold'),
#         ('Silver', 'Silver'),
#     )

#     name = models.CharField(max_length=250, choices=PACKAGE_NAME)
#     preview_description = models.CharField(max_length=255, verbose_name='Short Descriptions')
#     feature = RichTextField()
#     price = models.IntegerField()

#     def __str__(self):
#         return self.name


class CustomerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True, verbose_name='Address')

    def __str__(self):
        return self.name
 

class CompanyInfo(models.Model):
    # COMPANY_TYPE = (
    #     ('LLC', 'LLC'),
    #     ('S-Corporation', 'S-Corporation'),
    #     ('C-Corporation', 'C-Corporation'),
    #     ('Nonprofit', 'Nonprofit'),

    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # service_package = models.ForeignKey(Package, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    # company_type = models.CharField(max_length=50, choices=COMPANY_TYPE)
    company_contact = models.CharField(max_length=250)

    package_information = models.TextField(max_length=50, blank=True, null=True)

    company_location = models.TextField(verbose_name='Company Address')
    business_purpose = models.TextField()

    def __str__(self):
        return self.company_name



class Blog(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    short_description = models.TextField(max_length=500)
    blog_content = RichTextField()
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return str(self.blog_title)











#Dependency Add

# class Country(models.Model):
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name
#     class Meta:
#         # managed = True
#         db_table = 'myapp_country'

   
# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name
#     class Meta:
#         # managed = True
#         db_table = 'myapp_city'


# class Business(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
  
#     def __str__(self):
#         return self.name
#     class Meta:
#         # managed = True
#         db_table = 'myapp_business'
        
        
# class Package(models.Model):
#     business = models.ForeignKey(Business, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.name
#     class Meta:
#         # managed = True
#         db_table = 'myapp_package'
         

# class Person(models.Model):
#     name= models.CharField(max_length=100, verbose_name="Enter Your Comapny Email*")
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
#     business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True)
#     package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'Order Details'





# New Package add

class Country(models.Model):

    c_name = models.CharField(max_length=200, unique=True,primary_key=True)
  
    def __str__(self):
        return f'{str(self.c_name)}'


class Location(models.Model):
    c_name = models.ForeignKey(Country,null=True,blank=True,on_delete=models.CASCADE)
    l_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{str(self.c_name)} : {str(self.l_name)}'


class BusinessPlan(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value1 = models.PositiveIntegerField()
    value2 = models.PositiveIntegerField()
    value3 = models.PositiveIntegerField()


    def __str__(self):
        return f'{str(self.location)} : {str(self.name)} : {str(self.value1)} : {str(self.value2)} : {str(self.value3)}'

class SelectedPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    business_plan = models.ForeignKey(BusinessPlan, on_delete=models.CASCADE)
    value1 = models.PositiveIntegerField()
    value2 = models.PositiveIntegerField()
    value3 = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.country} - {self.location} - {self.business_plan}'