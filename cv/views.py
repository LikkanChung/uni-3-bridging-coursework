from django.shortcuts import render
from .models import Contact, Education, Experience, Volunteering
from django.utils import timezone

# Create your views here.
def cv(request):
    contact = Contact.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    education = Education.objects.filter(published_date__lte=timezone.now()).order_by('end_date')
    experience = Experience.objects.filter(published_date__lte=timezone.now()).order_by('end_date')
    volunteering = Volunteering.objects.filter(published_date__lte=timezone.now()).order_by('end_date')
    return render(request, 'cv/cv.html', {'contact': contact, 'education': education, 'experience': experience, 'volunteering': volunteering})
