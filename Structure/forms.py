from django.forms import ModelForm
from users.models import Student
from django.db.models import TextField,ImageField

class EditProfile(ModelForm):

    image = ImageField()

    class Meta:
        model = Student
        fields = ['image']

class EditProfiledes(ModelForm):

    description = TextField()

    class Meta:
        model = Student
        fields = ['description']



