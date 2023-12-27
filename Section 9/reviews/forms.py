from django import forms
from reviews.models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your Name",
#         max_length=50,
#         error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please Enter shorter name",
#         },
#     )
#     review_text = forms.CharField(
#         widget=forms.Textarea, max_length=200, label="Your Review"
#     )
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ['owner_comment']
        labels = {"user_name": "Your Name", "review_text": "Your Feedback"}
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please Enter shorter name",
            }
        }
