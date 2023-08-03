from .forms import NewsletterForm
from django.contrib import messages


def footer_renderer(request):
    news_letter_form = NewsletterForm(request.POST or None)
    if request.method == "POST":
        if news_letter_form.is_valid():
            news_letter_form.save()
            messages.add_message(request, messages.SUCCESS, "Success! Your message has been submitted.")
            news_letter_form = NewsletterForm()
    return {
        'news_letter_form': news_letter_form
    }
