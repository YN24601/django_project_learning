from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.urls import reverse

# Create your views here.
def rental_review(request):
    # Post Request  --> Form Content -->Thank you
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))
    # Else render the form
    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request):
    return render(request, 'cars/thank_you.html')