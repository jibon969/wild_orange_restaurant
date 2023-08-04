from django.shortcuts import render
from .models import (
    AboutUs,
    Cookies,
    Faq,
    Help,
    PolicyPolicy,
    TermsConditions,
)


def about_us(request):
    about_us = AboutUs.objects.all().first()
    context = {
        'about_us': about_us
    }
    return render(request, 'about_us/about_us.html', context)


def cookies(request):
    cookie = Cookies.objects.all().first()
    context = {
        'cookie': cookie
    }
    return render(request, 'about_us/cookies.html', context)


def faq(request):
    faq_queryset = Faq.objects.all().first()
    context = {
        'faq_queryset': faq_queryset
    }
    return render(request, 'about_us/faq.html', context)


def help_view(request):
    help = Help.objects.all().first()
    context = {
        'help': help
    }
    return render(request, 'about_us/help.html', context)


def privacy_policy(request):
    privacy = PolicyPolicy.objects.all().first()
    context = {
        'privacy': privacy
    }
    return render(request, 'about_us/privacy-privacy.html', context)


def terms_conditions(request):
    term_condition = TermsConditions.objects.all().first()
    context = {
        'term_condition': term_condition
    }
    return render(request, 'about_us/terms-and-conditions.html', context)

