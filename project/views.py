from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewProject, FilterProjectForm
from django.contrib import messages
from .models import Project
from django.contrib.auth.decorators import login_required
from main.views import videssur_required
import json
from datetime import date
from decimal import Decimal
from django.db.models import Q
from django.core.paginator import Paginator


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@login_required
@videssur_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('project_list')


@login_required
@videssur_required
def project_create(request):
    form = CreateNewProject(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewProject(request.POST, initial={
                                'ong': request.user.ong})
        if form.is_valid():
            project = form.save(commit=False)
            project.ong = request.user.ong
            project.save()
            return redirect('project_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    return render(request, 'project/register.html', {"form": form, "title": "Crear Proyecto", 'page_title': 'SarandONGa 💃 - Crear Proyecto'})


@login_required
@videssur_required
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = CreateNewProject(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CreateNewProject(instance=project)
    return render(request, 'project/register.html', {'form': form, 'title': 'Actualizar proyecto', 'page_title': 'SarandONGa 💃 - Actualizar Proyecto'})


@login_required
@videssur_required
def project_details(request, project_id):  # TODO
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project/project_details.html', {'project': project})


def get_query_str(request):
    query_str = ""
    keys = request.GET.keys()
    if "qsearch" in keys:
        query_str = "&qsearch="
        query_str += request.GET["qsearch"]
    if "start_date_min" in keys:
        query_str += "&start_date_min="
        query_str += request.GET["start_date_min"]
    if "start_date_max" in keys:
        query_str += "&start_date_max="
        query_str += request.GET["start_date_max"]
    if "end_date_min" in keys:
        query_str += "&end_date_min="
        query_str += request.GET["end_date_min"]
    if "end_date_max" in keys:
        query_str += "&end_date_max="
        query_str += request.GET["end_date_max"]
    if "number_of_beneficiaries_min" in keys:
        query_str += "&number_of_beneficiaries_min="
        query_str += request.GET["number_of_beneficiaries_min"]
    if "number_of_beneficiaries_max" in keys:
        query_str += "&number_of_beneficiaries_max="
        query_str += request.GET["number_of_beneficiaries_max"]
    if "amount_min" in keys:
        query_str += "&amount_min="
        query_str += request.GET["amount_min"]
    if "amount_max" in keys:
        query_str += "&amount_max="
        query_str += request.GET["amount_max"]
    if "announcement_date_min" in keys:
        query_str += "&announcement_date_min="
        query_str += request.GET["announcement_date_min"]
    if "announcement_date_max" in keys:
        query_str += "&announcement_date_max="
        query_str += request.GET["announcement_date_max"]

    return query_str


@login_required
@videssur_required
def project_list(request):
    # get projects dict from database
    objects = Project.objects.filter(ong=request.user.ong).values()

    form = FilterProjectForm(request.GET or None)
    if request.method == 'GET':
        objects = project_filter(objects, form)

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    project_page = paginator.get_page(page_number)

    projects_dict = [project for project in project_page]
    for p in projects_dict:
        p.pop('_state', None)
        # remove null values
        for key, value in list(p.items()):
            if value is None or value == '':
                p[key] = '-'

    project_json = json.dumps(projects_dict, cls=CustomJSONEncoder)

    query_str = get_query_str(request)

    context = {
        'objects': project_page,
        'objects_json': project_json,
        'object_name': 'proyecto',
        'object_name_en': 'project',
        'title': 'Gestión de Proyectos',
        'page_title': 'SarandONGa 💃 - Gestión de Proyectos',
        'form': form,
        'query_str': query_str
    }
    return render(request, 'project/list.html', context)


def is_valid_queryparam(param):
    return param != "" and param is not None


def project_filter(queryset, form):

    qsearch = form['qsearch'].value()
    start_date_min = form['start_date_min'].value()
    start_date_max = form['start_date_max'].value()
    end_date_min = form['end_date_min'].value()
    end_date_max = form['end_date_max'].value()
    number_of_beneficiaries_min = form['number_of_beneficiaries_min'].value()
    number_of_beneficiaries_max = form['number_of_beneficiaries_max'].value()
    amount_min = form['amount_min'].value()
    amount_max = form['amount_max'].value()
    announcement_date_min = form['announcement_date_min'].value()
    announcement_date_max = form['announcement_date_max'].value()

    if qsearch is not None:
        if qsearch.strip() != "":
            queryset = queryset.filter(
                Q(title__icontains=qsearch) | Q(country__icontains=qsearch))

    if is_valid_queryparam(start_date_min):
        queryset = queryset.filter(start_date__gte=start_date_min)

    if is_valid_queryparam(start_date_max):
        queryset = queryset.filter(start_date__lte=start_date_max)

    if is_valid_queryparam(end_date_min):
        queryset = queryset.filter(end_date__gte=end_date_min)

    if is_valid_queryparam(end_date_max):
        queryset = queryset.filter(end_date__lte=end_date_max)

    if is_valid_queryparam(number_of_beneficiaries_min):
        queryset = queryset.filter(
            number_of_beneficiaries__gte=number_of_beneficiaries_min)

    if is_valid_queryparam(number_of_beneficiaries_max):
        queryset = queryset.filter(
            number_of_beneficiaries__lte=number_of_beneficiaries_max)

    if is_valid_queryparam(amount_min):
        queryset = queryset.filter(amount__gte=amount_min)

    if is_valid_queryparam(amount_max):
        queryset = queryset.filter(amount__lte=amount_max)

    if is_valid_queryparam(announcement_date_min):
        queryset = queryset.filter(
            announcement_date__gte=announcement_date_min)

    if is_valid_queryparam(announcement_date_max):
        queryset = queryset.filter(
            announcement_date__lte=announcement_date_max)

    return queryset
