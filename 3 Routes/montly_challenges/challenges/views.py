from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
challenges_dict = {
    "january": "Complete a 30-day plank challenge.",
    "february": "Run 5 kilometers without stopping.",
    "march": "Do 100 push-ups in a single day.",
    "april": "Take the stairs instead of the elevator for a week.",
    "may": "Try a new type of workout class (e.g., yoga, kickboxing).",
    "june": "Commit to drinking at least 8 glasses of water every day for a month.",
    "july": "Achieve a personal best in your favorite cardio exercise (e.g., running, cycling).",
    "august": "Do a full-body workout using only bodyweight exercises.",
    "september": "Include at least one serving of vegetables in every meal for a week.",
    "october": "Practice mindfulness and meditation for 10 minutes each day for a month.",
    "november": "Complete a 7-day fitness challenge found online (e.g., HIIT, yoga, or dance).",
    "december": "",
}


def challenges(request):
    list_items = ""
    months = list(challenges_dict.keys())

    return render(request, "challenges/index.html", {"months": months})


def month_challenge_by_number(request, month):
    months = list(challenges_dict.keys())
    actual_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[actual_month])
    return HttpResponseRedirect(redirect_path)


def index(request, month):
    month = month.lower()

    if month in challenges_dict:
        challenge = challenges_dict[month]
        formatted_month = month
        formatted_challenge = challenge
        return render(
            request,
            "challenges/challenge.html",
            {"challenge_text": formatted_challenge, "month": formatted_month},
        )
    else:
        return HttpResponseBadRequest(f"<h1>No challenge found for this month</h1>")
