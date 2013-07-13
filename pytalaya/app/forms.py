from django.forms import ModelForm
from pytalaya.models. import Team

class TeamForm(ModelForm):
    class Meta:
        model = Team
	fields = '__all__'
