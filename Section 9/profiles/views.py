from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from profiles.forms import ProfileForm
from profiles.models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return redirect(reverse("profiles"))

#         return render(request, "profiles/create_profile.html", {"form": submitted_form})


class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
    fields = "__all__"



class ProfileListView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = 'profiles'


