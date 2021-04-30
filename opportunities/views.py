from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def events_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        sql_query = f"SELECT * FROM opportunities_event WHERE event_category='{search_query}'"
        objects = Event.objects.raw(sql_query)
        context = {
            'events': objects,
        }
        print(objects)
        return render(request, 'events.html', context)
    else:
        objects = Event.objects.raw("SELECT * FROM opportunities_event")
        context = {
            'events': objects,
        }
        print(objects)
        return render(request, 'events.html', context)
