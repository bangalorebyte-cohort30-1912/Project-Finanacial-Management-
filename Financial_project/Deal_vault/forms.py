from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from crispy_forms.layout import Submit
from django import forms

# class UserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email')

# class UserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ('username', 'email')

class TransactionForm(forms.Form):
    Name = forms.CharField(max_length=100)
    CHOICES = (('Income','Income'),('Expenses','Expenses'))
    input_Type = forms.ChoiceField(choices=CHOICES)
    amount = forms.IntegerField()
    options = (('Gpay','Gpay'),('Phonepe','Phonepe'),('Debit Card','Debit Card'),('Credit','Credit card'),('cash','cash'))
    Payment_method = forms.ChoiceField(choices=options)

    # def clean(self):
    #     cleaned_data = super(TransactionForm, self).clean()
    #     Name = cleaned_data.get('Name')
    #     input_Type = cleaned_data.get('input_Type')
    #     amount = cleaned_data.get('amount')
    #     if not Name and not input_Type and not amount:
    #         raise forms.ValidationError('You have to write something!')
    