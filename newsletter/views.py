from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import NewsletterSubscription

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})

def success(request):
    return render(request, 'newsletter/success.html')
