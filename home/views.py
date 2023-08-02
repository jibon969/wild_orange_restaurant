from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import (
    AboutImage,
    About,
    Services,
    Items,
    Category,
    OnlineTableBook,
    OurClient
)
from .forms import ContactForm, OnlineTableBookForm


def home(request):
    about_image = AboutImage.objects.all().first()
    about_info = About.objects.all()[:1]
    our_client = OurClient.objects.all()
    our_service = Services.objects.all()

    # OnlineTableBookForm
    booking_form = OnlineTableBookForm(request.POST or None)
    errors = None
    if booking_form.is_valid():
        booking_form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # Contact Form
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if form.errors:
        errors = form.errors

    context = {
        'about_image': about_image,
        'about_info': about_info,
        'our_service': our_service,
        'our_client': our_client,
        'booking_form': booking_form,
        'form': form,
        'errors': errors,
    }
    return render(request, "home/home.html", context)
