from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Event
from .myutils import Calendar
from datetime import datetime

# Create your views here.


def home(request):
    context = {"cal":Calendar().formatmonth(request.year,request.month,request.day)}

    return render(request,'accountability_app/home.html',context)


def event_detail(request, year,month,day):
    event = get_object_or_404(Event, date__year= year, date__month= month, date__day = day)
    return render(request, 'accountability_app/event_detail.html', {'event': event})

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