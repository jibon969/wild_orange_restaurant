from django.contrib import admin
from .models import (
    AboutUs,
    Cookies,
    Faq,
    Help,
    PolicyPolicy,
    TermsConditions,
)


# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = AboutUs


admin.site.register(AboutUs, AboutUsAdmin)


class CookiesAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = Cookies


admin.site.register(Cookies, CookiesAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = Faq


admin.site.register(Faq, FaqAdmin)


class HelpAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = Help


admin.site.register(Help, HelpAdmin)


class PolicyPolicyAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = PolicyPolicy


admin.site.register(PolicyPolicy, PolicyPolicyAdmin)


class TermsConditionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = TermsConditions


admin.site.register(TermsConditions, TermsConditionsAdmin)