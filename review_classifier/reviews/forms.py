from django import forms

class ReviewForm(forms.Form):
    review_text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 40}), label="Введите отзыв")
