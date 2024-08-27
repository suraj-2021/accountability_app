from django.shortcuts import render, redirect
from datetime import datetime
from .myutils import generate_month_calendar
from .forms import DayForm
from django.urls import reverse

year = datetime.now().year
month = datetime.now().month
def home(request):
    calendar_str = generate_month_calendar(year, month)

    return render(request, 'accountability_app/home.html',{"cal":calendar_str})

def day_details(request,year,month,day):
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:       
      form = DayForm()
    return render(request,'accountability_app/day_details.html',{"form": form})

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