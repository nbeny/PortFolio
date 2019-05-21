# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import Contact

def index(request):
    context = {
        "title":"nbeny index template",
        "content":"Bienvenue sur index.",
    }
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            contact = Contact()
            contact.Name = request.POST.get("Name")
            contact.Email = request.POST.get("Email")
            contact.Message = request.POST.get("Message")
            subject = 'Message de Alesio!'
            message = '%s %s' %(contact.Name, contact.Message)
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, contact.Email, emailTo, fail_silently=True)
            context['title_sender'] = 'Merci'
            context['confirm_message'] = "Merci pour le message. Nous allons revenir vers vous."
            context['contact'] = contact
            contact.save()

    if request.user.is_authenticated:
        context['premium_content'] = 'YEAHHHH, your authenticated :D'
    return render(request, "index/index.html", context)

