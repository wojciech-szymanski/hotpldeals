from django.forms import ModelForm
from .models import Deal

class DealForm(ModelForm):

    class Meta:
        model = Deal
        fields = ['title', 'url', 'upload']