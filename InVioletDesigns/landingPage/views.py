from django.shortcuts import render, redirect
from .models import photoGallery
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    photo_list = photoGallery.objects.order_by('name')

    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            email = EmailMessage('{}'.format(subject), '{}{}{}{}'.format(name, email, subject, message), to=['apechauer@gmail.com'])
            email.send()
            messages.success(request, 'Thanks {}. In Violet Designs will contact you shortly!'.format(name))
            return redirect('index')
        else:
            messages.warning(request, 'Form not valid')
    else:
        form = ContactForm()

    context = {'photo_list': photo_list, 'form': form}
    return render(request, 'landingPage/index.html', context)
