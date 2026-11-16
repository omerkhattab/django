
from django.http import HttpResponse, request
from django.shortcuts import render
from members.models import Member
from django.db.models import Count
def about(request):
    return render (request,"about.html")
def count(request):
      
    return HttpResponse("<p>Number of members: " + str(Member.objects.count()) + "</p>")

def hello(request):
    return HttpResponse("Hello omer!")
def members_page(request):
    
    return render(request, "members.html", {"members": Member.objects.all() , "count": Member.objects.count()})
def first(request):
   
    return render(request, "first.html", {"member": Member.objects.first()})
def active(request):
    actives = Member.objects.filter(active=True)
    return render(request,"active.html",{"members" : actives ,"count":actives.count()})
def duties(request):
    result = Member.objects.values("duty").annotate(total=Count("id")).order_by("duty")
        
    return render(request, "duties.html", {"duties": result})
def member_detail(request, name):
    member = Member.objects.filter(name=name).first()
    if member:
        return render(request, "member_detail.html", {"member": member})
    else:
        return HttpResponse("Member not found", status=404)

def duty_members(request,duty):
   duty_list = Member.objects.filter(duty=duty)
   if not duty_list:
      return HttpResponse("duty not found ",status=404)
   else :
      return render(request,"duty_members.html",{"members":duty_list , "duty":duty ,"count":duty_list.count()})