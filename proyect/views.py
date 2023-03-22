from django.shortcuts import redirect, get_object_or_404
from proyect.models import Proyect


def proyect_delete(request, proyect_id):
    proyect = get_object_or_404(Proyect, id=proyect_id)
    proyect.delete()
    return redirect('/')


