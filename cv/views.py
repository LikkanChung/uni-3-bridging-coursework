from django.shortcuts import render
from .models import Contact, Education, Experience, Volunteering
from django.utils import timezone
from .forms import ContactForm, EducationForm, ExperienceForm, VolunteeringForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def cv(request):
    contact = Contact.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    education = Education.objects.filter(published_date__lte=timezone.now()).order_by('end_date')
    experience = Experience.objects.filter(published_date__lte=timezone.now()).order_by('end_date')
    volunteering = Volunteering.objects.filter(published_date__lte=timezone.now()).order_by('end_date')
    return render(request, 'cv/cv.html', {'contact': contact, 'education': education, 'experience': experience, 'volunteering': volunteering})

def cv_add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ContactForm
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Add new Conact"})

def cv_edit_contact(request, pk):
    post = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/cv')
    else:
        form = ContactForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Edit Conact"})

def cv_add_education(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = EducationForm
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Add new Education"})

def cv_edit_education(request, pk):
    post = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/cv')
    else:
        form = EducationForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Edit Education"})

def cv_add_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ExperienceForm
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Add new Experience"})

def cv_edit_experience(request, pk):
    post = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/cv')
    else:
        form = ExperienceForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Edit Experience"})

def cv_add_volunteering(request):
    if request.method == "POST":
        form = VolunteeringForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = VolunteeringForm
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Add new Volunteering"})

def cv_edit_volunteering(request, pk):
    post = get_object_or_404(Volunteering, pk=pk)
    if request.method == "POST":
        form = VolunteeringForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/cv')
    else:
        form = VolunteeringForm(instance=post)
    return render(request, 'cv/cv_edit.html', {'form': form, 'model': "Edit Volunteering"})
