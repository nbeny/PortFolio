from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

def index(request):
    context = locals()
    template = 'index.html'
    return render(request, template, context)

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user'}
    template = 'profile.html'
    return render(request, template, context)

def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print(request.POST)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['comment'])
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from eCommerce'
        message = '%s %s' %(comment, name)
        emailForm = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailForm, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for this message. We will get right back to you."
        form = None

    context = {'title': title, 'form':form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request, template, context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)