from django import forms

class SubscriberForm(forms.Form):
    '''Subscription form for signing up for notifications

    all fields are independent'''
    phone_number = forms.CharField(max_length=200, required=False)
    twitter = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=False)
