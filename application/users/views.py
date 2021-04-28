from django.shortcuts import render
from .models import User, UserAddress

# Create your views here.

def search(request):
    return render(request, 'users/search.html')

def searchResult(request):
    user = None
    query1 = None
    query = None
    address1 = None
    if 'q' and 'p' in request.GET:
        query = request.GET.get('q')
        query1 = request.GET.get('p')
        user = User.objects.get(first_name=query, last_name__contains=query1)
        if 'o' in request.GET:
            query = request.GET.get('o')
            address1 = UserAddress.objects.get(user=user)
            if int(address1.number_of_address) > int(query):
                return render(request, 'users/result.html',{'user':user, 'address1':address1})
        if 'i' in request.GET:
            query = request.GET.get('i')
            address1 = UserAddress.objects.get(user=user)
            if int(address1.number_of_address) < int(query):
                return render(request, 'users/result.html',{'user':user, 'address1':address1})
        if 'u' in request.GET:
            query = request.GET.get('u')
            address1 = UserAddress.objects.get(user=user)
            if int(address1.number_of_address) == int(query):
                return render(request, 'users/result.html',{'user':user, 'address1':address1})