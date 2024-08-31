from django.shortcuts import render, redirect,get_object_or_404
from datetime import datetime
from .myutils import generate_month_calendar
from .forms import DayForm, UserRegisterForm, MessageForm
from django.urls import reverse, reverse_lazy
from . models import DayModel,Message
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DayForm
from django.contrib.auth import login as auth_login
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import authenticate

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('accountability_app:home'))
        else: 
            return render(request, 'accountability_app/register.html', {'form': form})
    else:
        form = UserRegisterForm()
        return   render(request,'accountability_app/register.html',{'form':form}) 



def home(request):
    if request.user.is_authenticated:
        year = datetime.now().year
        month = datetime.now().month
        calendar_str = generate_month_calendar(year, month)

        return render(request, 'accountability_app/home.html',{"cal":calendar_str})
    else:
        
        return redirect(reverse('accountability_app:register'))


def day_details(request, year, month, day):
   
    date = f"{year}-{month}-{day}"
    selected_date = datetime(year=int(year), month=int(month), day=int(day)).date()
    
    # This will return a queryset of Day objects for that date
    day_objects = DayModel.objects.filter(user = request.user,date=selected_date) 
    if request.method == 'POST':
            form = DayForm(request.POST)
            if form.is_valid():
                day_model_instance = form.save(commit=False)
                day_model_instance.user = request.user  # Associate the current user
                day_model_instance.save()
            return redirect(reverse('accountability_app:home'))
    else:
        form = DayForm()

    
    context = {
        "form": form,
        "day_objects": day_objects,  # Add the filtered objects to the context
        "selected_date": date,  # Optional: pass the selected date to the template
    }

    return render(request, 'accountability_app/day_details.html', context)



def login_view(request):
    #next_url = request.GET.get('next','/accountability_app/home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully logged in.')
            return redirect(reverse('accountability_app:home'))
        else:
            messages.error(request,'invalid username or password. Please try again!')
    return render(request,'accountability_app/login.html')

def logout_view(request):
    logout(request)  # Clear the user session
    return redirect(reverse_lazy('accountability_app:home'))  # Redirect to home after logout



def public_notes(request):
    notes = DayModel.objects.filter(is_public=True)
    return render(request,'accountability_app/public_notes.html',{"notes":notes})


def post_update(request,pk):
    post = get_object_or_404(DayModel,pk=pk)
    if request.method == "POST":
        form = DayForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'title': post.title, 'content': post.note,'date':post.date})
        else:
            form =DayForm(instance=post)
            return render(request,'post_update.html',{'form':form})

def post_delete(request,pk):
    post = get_object_or_404(DayModel,pk=pk)
    post.delete()
    return JsonResponse({'success':True})


@login_required
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect(reverse('accountability_app:inbox'))
    else:
        form = MessageForm()
        
    return render(request, 'accountability_app/send_message.html', {'form': form, 'recipient': recipient})


def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request,'accountability_app/inbox.html',{'messages': messages})
@login_required    
def user_list(request):
    users = User.objects.exclude(id= request.user.id)  # Exclude the current user
    return render(request, 'accountability_app/user_list.html', {'users': users})

def initiate_payment(request):
    amount = 0
    if request.method == "POST":
        
        amount_str = request.POST.get("amount", "")
        if not amount_str:
            return JsonResponse({"error": "Amount is required."}, status=400)
        
        try:
            amount = int(amount_str) * 100  # Convert to integer and multiply by 100
        except ValueError:
            return JsonResponse({"error": "Invalid amount."}, status=400)
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount" : amount,
            "currency": "INR",
            "receipt": "order reciept",
            "notes": {"email":"user_email@example.com",},

        }
        order = client.order.create(data=payment_data)

        #preparing the context for the payment page

        context =  {
            "key": settings.RAZORPAY_API_KEY,
            "amount": order["amount"],
            "currency": order["currency"],
            "name": "Your Company Name",
            "description": "Payment for your Product",

            
            "order_id": order["id"],    

        }
        return render(request,'accountability_app/payment.html',context)
    return render(request,'accountability_app/payment.html')

def payment_success(request):
    return render(request, "accountability_app/payment_success.html")

def payment_failed(request):
    return render(request, "accountability_app/payment_failed.html")
"""
def day_details(request,year,month,day):
    
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accountability_app:home')) 
    else:       
        form = DayForm()
        

    return render(request,'accountability_app/day_details.html',{"form": form})
"""
"""
class home(TemplateView):
      
    template_name = 'accountability_app/home.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Add additional context
        context['users'] = Calender
        return context
"""