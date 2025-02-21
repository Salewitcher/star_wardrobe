from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm

def contact_view(request):
    """ Handle contact form submission """
    if request.method == 'POST' and 'message' in request.POST:
        # Create and save the contact message instance
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()  # Save the form and get the instance
            
            # Optionally, retrieve the message content if needed
            user_message = contact_message.message
            
            # Show confirmation message with the user's message
            messages.success(request, f"Your message has been sent successfully: \"{user_message}\"")
            
            return redirect('contact')  # Redirect to the contact page after submission
        else:
            messages.error(request, "There was an error sending your message. Please try again.")
    else:
        form = ContactMessageForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
