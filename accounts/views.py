from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse
from .forms import (
    RegisterForm,
    LoginForm,
    UserProfileForm
)
from .models import EmailActivation
from django.views.generic import View
from django.views.generic.edit import FormMixin
from .forms import ActivateEmailForm


def register_view(request):
    """
    User registration view
    :param request:
    :return:
    """
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registration Successfully Completed')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Login view
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {email}")
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.WARNING, "You are successfully logout !")
    return redirect('login')


def profile_view(request):
    if request.user.is_authenticated:
        form = UserProfileForm(instance=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                profile = form.save(commit=False)  # Create unsaved instance
                # Modify the profile if needed
                # For example: profile.bio = form.cleaned_data['bio']
                profile.save()  # Save the modified profile
                messages.success(request, 'Profile successfully updated')
                return redirect('home')
        context = {
            'form': form,
            'user': request.user
        }
        return render(request, 'accounts/profile.html', context)
    else:
        messages.success(request, 'Create an account')
        return redirect('login')

#
# class AccountEmailActivateView(FormMixin, View):
#     """
#     E-mail activation for register user. default
#     """
#     success_url = '/login/'
#     form_class = ActivateEmailForm
#     key = None
#
#     def get(self, request, key=None, *args, **kwargs):
#         self.key = key
#         if key is not None:
#             qs = EmailActivation.objects.filter(key__iexact=key)
#             confirm_qs = qs.confirmable()
#             if confirm_qs.count() == 1:
#                 obj = confirm_qs.first()
#                 obj.activate()
#                 messages.success(request, "Your email has been confirmed. Please login.")
#                 # print("Your email has been confirmed. Please login.")
#                 return redirect("login")
#             else:
#                 activated_qs = qs.filter(activated=True)
#                 if activated_qs.exists():
#                     reset_link = reverse("password_reset")
#                     msg = """Your email has already been confirmed
#                     Do you need to <a href="{link}">reset your password</a>?
#                     """.format(link=reset_link)
#                     messages.success(request, mark_safe(msg))
#                     return redirect("login")
#         context = {'form': self.get_form(), 'key': key}
#         return render(request, 'accounts/registration/activation_error.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # create form to receive an email
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         msg = """Activation link sent, please check your email."""
#         # print("Activation link sent, please check your email.")
#         request = self.request
#         messages.success(request, msg)
#         email = form.cleaned_data.get("email")
#         obj = EmailActivation.objects.email_exists(email).first()
#         user = obj.user
#         new_activation = EmailActivation.objects.create(user=user, email=email)
#         new_activation.send_activation()
#         return super(AccountEmailActivateView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         context = {'form': form, "key": self.key}
#         return render(self.request, 'accounts/registration/activation_error.html', context)
