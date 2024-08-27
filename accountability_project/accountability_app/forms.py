from django.forms import ModelForm
from .models import DayModel

class DayForm(ModelForm):
    class Meta:
        model = DayModel
        fields = ('title','note','date')
