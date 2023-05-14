from dataclasses import fields
from django import forms
from bgd_consultancy_app.models import CustomerInfo, CompanyInfo, SelectedPlan

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = "__all__"
        exclude = ('user',)


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = "__all__"
        exclude = ('user',)


class SelectedPlanForm(forms.ModelForm):
    class Meta:
        model = SelectedPlan
        fields = ['user']



#Dependency Add

# class PersonForm(forms.ModelForm): 
#     class Meta:
#         model = Person
#         fields = ('name','country','city','business','package')
 
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['city'].queryset = City.objects.none()
 
#  #City..........
#         if 'country' in self.data:
#             try:
#                 country_id = int(self.data.get('country'))
#                 self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
                
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk and self.instance.country:
#             self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

# #Business...............
        
#          # Business
#         self.fields['business'].queryset = Business.objects.none()
#         if 'city' in self.data:
#             try:
#                 city_id = int(self.data.get('city'))
#                 self.fields['business'].queryset = Business.objects.filter(city_id=city_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk and self.instance.city:
#             self.fields['business'].queryset = self.instance.city.business_set.order_by('name')

# # Package.......................................
#         self.fields['package'].queryset = Package.objects.none()
#         if 'business' in self.data:
#             try:
#                 business_id = int(self.data.get('business'))
#                 self.fields['package'].queryset = Package.objects.filter(business_id=business_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk and self.instance.business:
#             self.fields['package'].queryset = self.instance.business.package_set.order_by('name')

