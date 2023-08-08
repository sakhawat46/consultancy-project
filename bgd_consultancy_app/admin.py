from django.contrib import admin
from bgd_consultancy_app.models import CustomerInfo, CompanyInfo, Blog

from .models import *

# Register your models here.

# admin.site.register(Package)
admin.site.register(CustomerInfo)
admin.site.register(CompanyInfo)


# admin.site.register([Person, Country, City])


class BlogAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('blog_title',)}

admin.site.register(Blog, BlogAdmin)








#Dependency Add

# admin.site.register(Person)
# admin.site.register(Country)
# admin.site.register(City)
# admin.site.register(Business)
# admin.site.register(Package)


# New Dependency Add

admin.site.register(Country)
admin.site.register(Location)
admin.site.register(BusinessPlan)
# admin.site.register(SelectedPlan)