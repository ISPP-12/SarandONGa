from django.shortcuts import render
from datetime import datetime
import json
from donation.models import Donation
from decimal import Decimal

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


# Create your views here.
def donations_list(request):
    # get donations from database
    donations = Donation.objects.all()
    

    for donation in donations:
        created_date = donation.created_date
        modified_date = created_date.strftime('%d/%m/%Y')
        donation.created_date = modified_date

    donations_dict = [obj.__dict__ for obj in donations]
    for d in donations_dict:
        d.pop('_state', None)

    donations_json = json.dumps(donations_dict, cls=CustomJSONEncoder)


    return render(request, 'donation/list.html', {'objects': donations, 'objects_json': donations_json, 'object_name': 'donación', 'title': 'Gestión de donaciones'})