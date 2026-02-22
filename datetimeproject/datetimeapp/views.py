from django.shortcuts import render
from datetime import datetime

def show_datetime(request):
    now = datetime.now()
    return render(request, 'datetimeapp/datetime.html', {
        'current_datetime': now
    })