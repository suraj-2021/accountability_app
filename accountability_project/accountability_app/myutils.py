from calendar import HTMLCalendar
from datetime import datetime
from django.urls import reverse


class Calendar(HTMLCalendar):

    def formatday(self,day,month,year):
         if day == 0:
            return '<td class = "noday"> </td>' 
         
         #create a URL for the day
         url= reverse('event_detail',kwargs={"year":year,"month":month, "day":day})
         return f'<td class="day"> <a href="{url}"> {day} </a> </td>'
    
    def formatmonth(self,year, month, withyear=True):
     
        return super().formatmonth(year, month,withyear)