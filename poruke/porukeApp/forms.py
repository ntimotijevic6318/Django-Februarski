from django.forms import ModelForm
from .models import  Telefoni

class TelefoniForm(ModelForm):
    class Meta:
        model = Telefoni
        fields = [ 'markaTelefona' , 'modelTelefona']
