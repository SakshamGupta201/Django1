from django.shortcuts import redirect, render

# Create your views here.


def thank_you(request):
    return render(request, "reviews/thankyou.html")


def review(request):
    if request.method == "POST":
        try:
            if request.POST.get("username") == "":
                return render(request, "reviews/review.html", {"has_error": True})
            else:
                return redirect(thank_you)
        except:
            pass
    return render(request, "reviews/review.html", {"has_error": False})
