from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Customer
from checkout.models import CustomerOrder
from videos.models import Video, UserRating, UserReview
from .forms import SavedAddressForm, SavedDetailsForm, MessageForm
from customer.models import CustomerMessageThread, CustomerMessage

# Create your views here.

def customer_info(request):
    """
    """
    customer = get_object_or_404(Customer, user=request.user)
    order_history = CustomerOrder.objects.filter(customer=customer)

    context = {
        'customer': customer,
        'order_history': order_history,
    }

    return render(request, 'customer/customer_info.html', context)


def update_info(request):
    """
    """
    user = request.user

    if request.method == 'POST':
        saved_details_form = SavedDetailsForm(request.POST, instance=user)
        if saved_details_form.is_valid():
            saved_details = saved_details_form.save(commit=False)
            saved_details.save()
            messages.success(request, 'Your details have been saved.')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        saved_details_form = SavedDetailsForm()
    
    saved_details_form = SavedDetailsForm()

    context = {
        'user': user,
        'saved_details_form': saved_details_form,
    }

    return render(request, 'customer/update_info.html', context)



def saved_address(request):
    
    customer = get_object_or_404(Customer, user=request.user)

    if request.method == 'POST':
        saved_address_form = SavedAddressForm(request.POST, instance=customer)
        if saved_address_form.is_valid():
            saved_address = saved_address_form.save(commit=False)
            saved_address.save()
            messages.success(request, 'Your address has been saved.')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        saved_address_form = SavedAddressForm()
    
    saved_address_form = SavedAddressForm()

    context = {
        'customer': customer,
        'saved_address_form': saved_address_form,
    }

    return render(request, 'customer/saved_address.html', context)

def read_reviews(request):
    """
    """

    star_ratings = UserRating.objects.filter(user=request.user)
    user_reviews = UserReview.objects.filter(author=request.user)

    context = {
        'star_ratings': star_ratings,
        'user_reviews': user_reviews,
    }

    return render(request, 'customer/reviews.html', context)

def create_messages(request):
    """
    """
    if request.method == "POST":
        message_form = MessageForm(request.POST)

        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.user = request.user
            message.thread = CustomerMessageThread.objects.create(
                user = request.user,
                order_number = message.order_number,
                subject = message.subject,
                user_email = message.user_email,
            )
            message.save()
            messages.success(request, 'Your message has been saved.')
            return redirect('read_messages')
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        message_form = MessageForm()


    context = {
        'message_form': message_form,
    }

    return render(request, 'customer/create_messages.html', context)

def read_messages(request):
    """
    View to read customer messages in a specific thread.
    """
    # Get the threads associated with the user
    thread = CustomerMessageThread.objects.filter(user=request.user)
    customer_messages = None
    message_query = None

    if request.GET:
        # Get the thread ID from the request
        message_query = request.GET.get('thread')
        if message_query:
            # Filter messages by the specified thread and order by date
            customer_messages = CustomerMessage.objects.filter(thread=message_query).order_by('-date')

    # Prepare the context for rendering the template
    context = {
        'customer_messages': customer_messages,
        'thread': thread,
        'message_query': message_query,
    }

    # Render the template with the context
    return render(request, 'customer/read_messages.html', context)



def view_wishlist(request):
    wishlist = []
    videos = Video.objects.all()

    for video in videos:
        if video.wishlist.filter(id=request.user.id).exists():
            wishlist.append(video)

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'customer/wishlist.html', context)

def order_detail(request, order_number):
    """
    """
    

    return render(request, 'customer/order_detail.html')


def reply_messages(request, thread):

    customer_messages = CustomerMessage.objects.filter(thread=thread)
    message_thread = get_object_or_404(CustomerMessageThread, id=thread)
    email = message_thread.user_email
    subject = f"RE: {message_thread.subject}"
    order_number = message_thread.order_number

    if request.method == "POST":
        message_form = MessageForm(request.POST, initial={'user_email': email, 'subject': subject, 'order_number': order_number,})
        print(message_form)

        if message_form.is_valid():        
            message = message_form.save(commit=False)
            message.user = request.user
            message.thread = message_thread
            message.save()

            messages.success(request, 'Your message has been saved.')
            url = reverse('read_messages') + f'?thread={thread}'
            return HttpResponseRedirect(url)
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        message_form = MessageForm(initial={'user_email': email, 'subject': subject, 'order_number': order_number,})

    context = {
        'message_form': message_form,
        'customer_messages': customer_messages,
        'message_thread': message_thread,
    }

    return render(request, 'customer/reply_messages.html', context)


