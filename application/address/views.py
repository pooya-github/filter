from django.shortcuts import render
from users.models import User, UserAddress

# Create your views here.

def insert(request):
    return render(request, 'address/data.html')

def register(request):
    if request.method=="POST":
        q = request.POST['id']
        s = request.POST['subject']
        c = request.POST['coordination']
        user = User.objects.get(id=q)
        u = UserAddress(subject=s,user=user,coordination=c)
        u.save()
        send_notification()

def send_notification(request):
    print("One new address is created")