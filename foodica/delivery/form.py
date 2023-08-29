from django import forms
from django.db.models import fields
from delivery.models import delivery

class DeliveryForm(forms.ModelForm):
    gender = (('Male','Male'),('Female', 'Female'),('Others', 'Others'))
    gender = forms.ChoiceField(choices=gender,widget=forms.RadioSelect)

    vehicle = (('Bicycle', 'Bicyce'),('Bike','Bike'),('Other','Other'))
    vehicle = forms.ChoiceField(choices=vehicle,widget=forms.RadioSelect)

    Identity = (('Pancard', 'Pancard'),('Adharcard','Adharcard'),('Other','Other'))
    Identity = forms.ChoiceField(choices=Identity,widget=forms.RadioSelect)

    class Meta:
        model = delivery
        fields = "__all__"