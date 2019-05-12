from django.forms import Form, ModelForm, ModelChoiceField, BooleanField

from .models import Mentor


class CreateMentorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateMentorForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['available'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Mentor
        fields = ['email', 'first_name', 'last_name', 'phone', 'available', ]


class FindMentorForm(Form):
    mentor = ModelChoiceField(
        queryset=Mentor.objects.none(), empty_label="------------")
    available = BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mentor'].widget.attrs['class'] = 'form-control'
        self.fields['available'].widget.attrs['class'] = 'form-check-input'

        if 'available' in self.data:
            try:
                self.fields['mentor'].queryset = Mentor.objects.filter(
                    available=True)
            except (ValueError, TypeError):
                pass
        else:
            try:
                self.fields['mentor'].queryset = Mentor.objects.filter(
                    available=False)
            except (ValueError, TypeError):
                pass
