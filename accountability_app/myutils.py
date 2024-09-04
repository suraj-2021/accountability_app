import calendar
from django.urls import reverse

def generate_month_calendar( year:int, month: int):
    month_calendar = calendar.monthcalendar(year, month)
   
    # Define the HTML for the calendar with CSS styles
    html = '''
    <style>
        .calcolor { 
            background-color: #f0f8ff; /* Light blue background for all cells */
        }
        .calcolor:hover {
            background-color: #add8e6; /* Darker blue on hover */
        }
        .empty-cell {
            background-color: #f5f5f5; /* Light gray background for empty cells */
        }
    </style>
    <script>
  <script>
    const redirectUrl = "{% url 'accountability_app:public_notes' %}";
    
    function redirectToUrl() {
        window.location.href = redirectUrl;
    }
</script>
  
    <table border="1" style="border-collapse: collapse; text-align: center;">
    '''
    html += f'<tr><th colspan="7"><button class ="minus" type="submit" style="background-color:green" onclick="redirectToUrl()" id="decrement"><</button>{calendar.month_name[month]} {year}<button style="background-color:green;" class ="plus" type="submit" id="increment">></button></th></tr>'
    html += '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>'

    for week in month_calendar:
        html += '<tr>'
        for day in week:
            
            if day == 0:
                html += '<td class="empty-cell"></td>'  # Empty cell for days outside the month
            else:
                day_link = reverse('accountability_app:day_details', args=[year, month, day])
                html += f'<td class="calcolor"><a href="{day_link}">{day}</a></td>'
        html += '</tr>'
    
    html += '</table>'
    return html
