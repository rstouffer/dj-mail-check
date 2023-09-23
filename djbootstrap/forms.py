from django import forms
from phone_field import PhoneFormField
from localflavor.us.forms import USStateField

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)

    company_name = forms.CharField(label="Company", max_length=100, required=False)

    address_l1 = forms.CharField(label="Address Line 1", max_length=100)
    address_l2 = forms.CharField(label="Address Line 2", max_length=100, required=False)

    city = forms.CharField(max_length=100)
    state = USStateField()
    zip_code = forms.CharField(label="Zip Code", max_length=5)

    phone = PhoneFormField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['autocomplete'] = 'off'
        self.fields['password'].widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['last_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['company_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['address_l1'].widget.attrs['autocomplete'] = 'off'
        self.fields['address_l2'].widget.attrs['autocomplete'] = 'off'
        self.fields['city'].widget.attrs['autocomplete'] = 'off'
        self.fields['state'].widget.attrs['autocomplete'] = 'off'
        self.fields['zip_code'].widget.attrs['autocomplete'] = 'off'
        self.fields['phone'].widget.attrs['autocomplete'] = 'off'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off' 
        self.fields['password'].widget.attrs['autocomplete'] = 'off'

class ChangeInfo(forms.Form):
    prevPassword = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True, label="Old Password")
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, required=False)
    newPassword = forms.CharField(label="New Password", max_length=100, widget=forms.PasswordInput, required=False)
    
    first_name = forms.CharField(label="First Name", max_length=100, required=False)
    last_name = forms.CharField(label="Last Name", max_length=100, required=False)

    company_name = forms.CharField(label="Company", max_length=100, required=False)

    address_l1 = forms.CharField(label="Address Line 1", max_length=100, required=False)
    address_l2 = forms.CharField(label="Address Line 2", max_length=100, required=False)

    city = forms.CharField(max_length=100, required=False)
    state = USStateField(required=False)
    zip_code = forms.CharField(label="Zip Code", max_length=5, required=False)

    phone = PhoneFormField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['autocomplete'] = 'off'
        self.fields['prevPassword'].widget.attrs['autocomplete'] = 'off'
        self.fields['newPassword'].widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['last_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['company_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['address_l1'].widget.attrs['autocomplete'] = 'off'
        self.fields['address_l2'].widget.attrs['autocomplete'] = 'off'
        self.fields['city'].widget.attrs['autocomplete'] = 'off'
        self.fields['state'].widget.attrs['autocomplete'] = 'off'
        self.fields['zip_code'].widget.attrs['autocomplete'] = 'off'
        self.fields['phone'].widget.attrs['autocomplete'] = 'off'

class SetUsername(forms.Form):
    username = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'

class SetPassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['autocomplete'] = 'off'

class SetEmail(forms.Form):
    email = forms.EmailField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = 'off'