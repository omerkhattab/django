from django.shortcuts import render

# Create your views here.

def group_list(request):
    return render(request, 'groups/group_list.html', {'groups': ['Group 1', 'Group 2', 'Group 3']})
