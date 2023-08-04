from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.about_us, name="about-us"),
    path('cookies/', views.cookies, name="cookies"),
    path('faq/', views.faq, name="faq"),
    path('help/', views.help_view, name="help"),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('terms-conditions/', views.terms_conditions, name="terms-conditions"),
]
