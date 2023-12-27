from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse
from reviews.forms import ReviewForm
from django.views import View

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from reviews.models import Review

# Create your views here.


class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works"
        return context


# class ReviewView(View):
#     def get(self, request):
#         review_form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": review_form})

#     def post(self, request):
#         review_form = ReviewForm(request.POST)

#         if review_form.is_valid():
#             review_form.save()
#             return redirect(reverse("thank_you"))
#         return render(request, "reviews/review.html", {"form": review_form})


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank_you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank_you"


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["reviews"] = Review.objects.all()
#         return context


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         context["review"] = Review.objects.get(pk=review_id)
#         return context


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = Review.objects.get(pk=request.session.get('fav_review')) == loaded_review
        context["fav_review"] = fav_id
        return context
    


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")
        request.session["fav_review"] = review_id
        return redirect(reverse("single_review", kwargs={"pk": review_id}))
