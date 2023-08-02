from django.contrib import admin
from .models import (
    AboutImage,
    About,
    Services,
    Category,
    Items,
    OnlineTableBook,
    OurClient,
    Contact
)


class AboutImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = AboutImage


admin.site.register(AboutImage, AboutImageAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = About


admin.site.register(About, AboutAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = Services


admin.site.register(Services, ServicesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = Items


admin.site.register(Items, ItemsAdmin)


class OnlineTableBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_people', 'timestamp']
    search_fields = ['name']
    list_per_page = 20

    class Meta:
        model = OnlineTableBook


admin.site.register(OnlineTableBook, OnlineTableBookAdmin)


class OurClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp']
    search_fields = ['name']
    list_per_page = 20

    class Meta:
        model = OurClient


admin.site.register(OurClient, OurClientAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp']
    search_fields = ['name']
    list_per_page = 20

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
