from django.shortcuts import render
from django.http import Http404

tasks = {
    "sunday": "Plan the week ahead.",
    "monday": "Prepare for meetings.",
    "tuesday": "Grocery shopping.",
    "wednesday": "Workout session.",
    "thursday": "Clean the house.",
    "friday": "Family movie night.",
    "saturday": "Gardening and relaxation."
}

def index(request):
    days = list(tasks.keys())
    return render(request, 'index.html', {'days': days})

def day_task(request, day):
    day_lower = day.lower()
    if day_lower not in tasks:
        raise Http404("Day not found")
    task = tasks[day_lower]
    return render(request, 'day.html', {'day': day_lower.capitalize(), 'task': task})
