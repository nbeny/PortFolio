from django import forms

length = 255

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=length, required=True, widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'type':'text',
            'placeholder':'fullname',
        }
    ),
        error_messages = {
            'required' : "This fullname is required",
            'invalid' : "This fullname is invalid"
    })
    Email = forms.CharField(max_length=length, required=True, widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'type':'text',
            'placeholder':'email',
        }
    ),
        error_messages = {
            'required' : "This email is required",
            'invalid' : "This email is invalid"
    })
    Message = forms.CharField(max_length=length, required=True, widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'type':'text',
            'placeholder':'message',
        }
    ),
        error_messages = {
            'required' : "This content is required",
            'invalid' : "This content is invalid"
    })

    # def clean(self):
    #     cleaned_data = super().clean()
        
    #     Email = self.cleaned_data.get('Email')
    #     Name = self.cleaned_data.get('Name')

    #     # if not 'gmail' or not 'outlook':
    #         # raise forms.ValidationError('Email has to be gmail or outlook')

    #     return Email, Name, cleaned_data
#Do Stuff