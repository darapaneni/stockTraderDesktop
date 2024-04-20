from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json

def line_chart(request):
    labels = json.dumps(["January", "February", "March", "April", "May", "June", "July"])
    data = json.dumps([0, 10, 5, 2, 20, 30, 45])
    return render(request, 'myapp/chart.html', {'labels': labels, 'data': data})

