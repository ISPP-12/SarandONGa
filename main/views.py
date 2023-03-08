from django.shortcuts import render
from datetime import datetime
from django.core import serializers
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def donations_list(request):
    # array of donations
    donations = [
        {   
            'id': 1,
            'title': 'New donation',
            'description': 'This is a new donation', # optional
            'date': '2020-01-10',
            'amount': 100,
            'donor_name': 'John',
            'donor_surname': 'Doe',
            'donor_email': 'johndoe@mail.com'
        },
        {   
            'id': 2,
            'title': 'Another donation',
            # 'description': 'This is a new donation', # optional
            'date': '2023-03-05',
            'amount': 80,
            'donor_name': 'Jane',
            'donor_surname': 'Doe',
            'donor_email': 'janedoe@mail.com'
        }
    ]

    for donation in donations:
        donation['date'] = datetime.strptime(donation['date'], '%Y-%m-%d').strftime('%d/%m/%Y')

    donations_json = json.dumps(donations)

    return render(request, 'donation/list.html', {'donations': donations, 'donations_json': donations_json})



    