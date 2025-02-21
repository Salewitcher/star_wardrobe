from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to the contact page
        else:
            messages.error(request, "There was an error sending your message. Please try again.")
    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact.html', {'form': form})
