from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import (
    AboutImage,
    About,
    Services,
    Item,
    Category,
    OurClient,
    YoutubeVideo,
)
from .forms import ContactForm, OnlineTableBookForm


def home(request):
    category = Category.objects.get(slug__icontains="breakfast")
    breakfast = Item.objects.filter(category=category).all()

    launch_slug = Category.objects.get(slug__icontains="launch")
    launch = Item.objects.filter(category=launch_slug).all()

    dinner_slug = Category.objects.get(slug__icontains="dinner")
    dinner = Item.objects.filter(category=dinner_slug).all()

    about_image = AboutImage.objects.all().first()
    about_info = About.objects.all()[:1]
    our_client = OurClient.objects.all()
    our_service = Services.objects.all()

    videos = YoutubeVideo.objects.values('video')[:1]
    # OnlineTableBookForm
    booking_form = OnlineTableBookForm(request.POST or None)
    errors = None
    if booking_form.is_valid():
        booking_form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Your message has been submitted.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # Contact Form
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Your message has been submitted..")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if form.errors:
        errors = form.errors

    context = {
        'about_image': about_image,
        'about_info': about_info,
        'category': category,
        'breakfast': breakfast,
        'launch': launch,
        'dinner': dinner,
        'our_service': our_service,
        'our_client': our_client,
        'videos': videos,
        'booking_form': booking_form,
        'form': form,
        'errors': errors,
    }
    return render(request, "home/home.html", context)


def category_item_list(request):
    category = Category.objects.get(id=1)
    items = Item.objects.filter(category=category)

    context = {
        'category': category,
        'items': items,
    }

    return render(request, "home/home.html", context)
