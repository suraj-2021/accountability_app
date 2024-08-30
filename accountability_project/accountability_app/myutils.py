import calendar
from django.urls import reverse

def generate_month_calendar(year: int, month: int) -> str:


    month_calendar = calendar.monthcalendar(year, month)

   
    html = '<table border="1" style="border-collapse: collapse; text-align: center;">'
    html += f'<tr><th colspan="7">{calendar.month_name[month]} {year}</th></tr>'
    html += '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>'

    for week in month_calendar:
        html += '<tr>'
        for day in week:
            if day == 0:
                html += '<td></td>'  # Empty cell for days outside the month
            else:
                day_link = reverse('accountability_app:day_details', args=[year,month,day])
                html += f'<td><a href="{day_link}">{day}</a> </td>'
        html += '</tr>'
    
    html += '</table>'
    return html