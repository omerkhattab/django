
from pathlib import Path
from django.conf import settings
from django.http import HttpResponse, request
import json
from django.shortcuts import render
def load_members():
    data_file = Path(settings.BASE_DIR).parent / "members.json"
    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
def about(request):
    return render (request,"about.html")
def count(request):
    data = load_members()       
    return HttpResponse("<p>Number of members: " + str(len(data)) + "</p>")

def hello(request):
    return HttpResponse("Hello omer!")
def members_page(request):
    data = load_members()
    return render(request, "members.html", {"members": data , "count": len(data)})
def first(request):
    data = load_members()
    return render(request, "first.html", {"member": data[0]})
def active(request):
    data = load_members()
    actives = []
    for member in data :
        if member["active"] :
            actives.append(member)
    return render(request,"active.html",{"members" : actives , "status":True,"count":len(actives)})
def duties(request):
    data = load_members()
    counts = {}
    for member in data:
        key = member["duty"]
        current_count = counts.get(key, 0)
        counts[key] = current_count + 1
    return render(request, "duties.html", {"duties": counts})
def member_detail(request, name):
    data = load_members()
    member = next((m for m in data if m["name"] == name), None)
    if member:
        return render(request, "member_detail.html", {"member": member})
    else:
        return HttpResponse("Member not found", status=404)

def duty_members(request,duty):
   data = load_members()
   duty_list = []
   for member in data :
      if member["duty"] == duty :
         duty_list.append(member)
   if not duty_list:
      return HttpResponse("duty not found ",status=404)
   else :
      return render(request,"duty_members.html",{"members":duty_list , "duty":duty ,"count":len(duty_list)})