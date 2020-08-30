from django import forms
from .models import Contact, Education, Experience, Volunteering

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('type', 'detail')

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('name', 'school', 'location', 'start_date', 'end_date', 'text')

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('role', 'location', 'start_date', 'end_date', 'text')

class VolunteeringForm(forms.ModelForm):
    class Meta:
        model = Volunteering
        fields = ('role', 'location', 'start_date', 'end_date', 'text')
