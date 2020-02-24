from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
 
from django.urls import reverse_lazy
from .forms import TransactionForm,User
from django.views.generic import CreateView
from .models import Transactions

# Create your views here.
def get_info(request):
    print("inside_info")
    if request.method == 'POST' :
        form = TransactionForm(request.POST)
        if form.is_valid():
            print("something")
            name = form.cleaned_data['Name']
            types = form.cleaned_data['input_Type']
            amount = form.cleaned_data['amount']
            Payment_method = form.cleaned_data['Payment_method']
            p = User.objects.filter(username=request.user).first()
            print(p)
            p_obj = Transactions(user=p,transaction_name=name, transaction_type=types, amount=amount, Payment_method=Payment_method, email=p)
            p_obj.save()
            print("something")
            return HttpResponseRedirect('/#')
    else:
        form = TransactionForm()
    context = {}
    p = User.objects.filter(username=request.user).first()
    print(p)
    queryset = Transactions.objects.filter(user=p)
    context['Transaction_list'] = queryset
    context['form'] = form      
    print(context['Transaction_list'])
    for i in queryset:
        print(i)
    # context['Leads'] = queryset
    # print(context['Leads'])
    return render(request,'Deal_vault/profile.html',context)




def uilogout(request):
    logout(request)

    return render(request, 'Deal_vault/profile.html')

# class SignUp(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'



