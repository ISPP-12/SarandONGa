from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import CreatePaymentForm, FilterPaymentForm
from .models import Payment, Project
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from main.views import custom_403
from django.db.models import Q
from django.core.paginator import Paginator
from person.models import GodFather
from home.models import Home


@login_required
def payment_create(request):
    if "godfather" in request.GET:
        godfather = GodFather.objects.get(id=request.GET.get("godfather"))
        project = None
        home = None
    elif "project" in request.GET:
        project = Project.objects.get(id=request.GET.get("project"))
        godfather = None
        home = None
    elif "home" in request.GET:
        home = Home.objects.get(id=request.GET.get("home"))
        godfather = None
        project = None
    else:
        godfather = None
        project = None
        home = None
    if request.method == "POST":
        form = CreatePaymentForm(
            request.user.ong,
            request.POST,
            initial={
                "ong": request.user.ong,
                "project": project,
                "godfather": godfather,
                "home": home,
            },
        )

        if form.is_valid():
            payment = form.save(commit=False)
            payment.ong = request.user.ong

            payment.save()

            return redirect(reverse("payment_create") + "?" + request.GET.urlencode())
        else:
            messages.error(request, "El formulario presenta errores")
    else:
        form = CreatePaymentForm(
            request.user.ong,
            initial={
                "ong": request.user.ong,
                "project": project,
                "godfather": godfather,
                "home": home,
            },
        )
    all_events = None
    if "godfather" in request.GET:
        all_events = Payment.objects.filter(
            ong=request.user.ong, godfather=request.GET.get("godfather")
        )
    elif "project" in request.GET:
        all_events = Payment.objects.filter(
            ong=request.user.ong, project=request.GET.get("project")
        )
    elif "home" in request.GET:
        all_events = Payment.objects.filter(
            ong=request.user.ong, home=request.GET.get("home")
        )
    else:
        all_events = Payment.objects.filter(ong=request.user.ong)
    event_arr = []
    for i in all_events:
        event_sub_arr = {}
        event_sub_arr["title"] = "{} - {}€".format(i.concept, i.amount)
        start_date = i.payday
        end_date = i.payday
        event_sub_arr["start"] = start_date
        event_sub_arr["url"] = f"/payment/{i.id}/update"
        event_sub_arr["end"] = end_date
        event_arr.append(event_sub_arr)
    datatest = json.dumps(event_arr, default=str)

    context = {
        "form": form,
        "title": "Añadir pago",
        "page_title": "SarandONGa 💃 - Añadir pago",
        "events_json": datatest,
    }

    return render(request, "payment/payment_form.html", context)


@login_required
def payment_update(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    form = CreatePaymentForm(request.user.ong, instance=payment)
    if request.user.ong == payment.ong:
        if request.method == "POST":
            form = CreatePaymentForm(
                request.user.ong, request.POST, request.FILES, instance=payment
            )
            if form.is_valid():
                form.save()
                return redirect(
                    reverse("payment_create") + "?" + request.GET.urlencode()
                )
        else:
            all_events = None
            if "godfather" in request.GET:
                all_events = Payment.objects.filter(
                    ong=request.user.ong, godfather=request.GET.get("godfather")
                )
            elif "project" in request.GET:
                all_events = Payment.objects.filter(
                    ong=request.user.ong, project=request.GET.get("project")
                )
            elif "home" in request.GET:
                all_events = Payment.objects.filter(
                    ong=request.user.ong, home=request.GET.get("home")
                )
            else:
                all_events = Payment.objects.filter(ong=request.user.ong)
            event_arr = []
            for i in all_events:
                event_sub_arr = {}
                event_sub_arr["title"] = "{} - {}€".format(i.concept, i.amount)
                start_date = i.payday
                end_date = i.payday
                event_sub_arr["start"] = start_date
                event_sub_arr["end"] = end_date
                event_sub_arr["url"] = f"/payment/{i.id}/update"
                event_sub_arr["id"] = str(i.id)
                event_arr.append(event_sub_arr)
            events_json = json.dumps(event_arr, default=str)

        context = {
            "form": form,
            "title": "Actualizar pago",
            "events_json": events_json,
            "page_title": "SarandONGa 💃 - Actualizar pago",
        }
    else:
        return custom_403(request)
    return render(request, "payment/payment_form.html", context)


@login_required
def payment_list(request):
    form = FilterPaymentForm(request.GET or None)
    objects = Payment.objects.filter(ong=request.user.ong).values()

    if request.method == "GET":
        objects = payment_filter(objects, FilterPaymentForm(request.GET))

    paginator = Paginator(objects, 12)
    page_number = request.GET.get("page")
    payment_page = paginator.get_page(page_number)

    context = {
        "objects": payment_page,
        "objects_name": "Payment",
        "title": "Gestión de Pagos",
        "page_title": "SarandONGa 💃 - Gestión de Pagos",
        "form": form,
    }

    return render(request, "payment/payment_list.html", context)


@login_required
def payment_delete(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.user.ong == payment.ong:
        payment.delete()
    else:
        return custom_403(request)
    return redirect("/payment/create")


@login_required
def payment_details(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.user.ong == payment.ong:
        return render(
            request,
            "payment/payment_details.html",
            {"payment": payment, "page_title": "SarandONGa 💃 - Detalles de pago"},
        )
    else:
        return custom_403(request)


def is_valid_queryparam(param):
    return param != "" and param is not None


def payment_filter(queryset, form):
    q = form["qsearch"].value()
    min_payday_date = form["min_payday_date"].value()
    max_payday_date = form["max_payday_date"].value()
    concept = form["concept"].value()
    ong = form["ong"].value()
    paid = form["paid"].value()
    godfather = form["godfather"].value()
    project = form["project"].value()
    amount_min = form["amount_min"].value()
    amount_max = form["amount_max"].value()

    if q is not None:
        if q.strip() != "":
            queryset = queryset.filter(
                Q(ong__name__icontains=q)
                | Q(godfather__name__icontains=q)
                | Q(project__title__icontains=q)
                | Q(concept__icontains=q)
            )

    if is_valid_queryparam(min_payday_date):
        queryset = queryset.filter(payday__gte=min_payday_date)

    if is_valid_queryparam(max_payday_date):
        queryset = queryset.filter(payday__lte=max_payday_date)

    if is_valid_queryparam(concept):
        queryset = queryset.filter(concept=concept)

    if is_valid_queryparam(ong):
        queryset = queryset.filter(ong__name=ong)

    if is_valid_queryparam(paid):
        queryset = queryset.filter(paid=paid)

    if is_valid_queryparam(godfather):
        queryset = queryset.filter(godfather__name=godfather)

    if is_valid_queryparam(project):
        queryset = queryset.filter(project__title=project)

    if is_valid_queryparam(amount_min):
        queryset = queryset.filter(amount__gte=amount_min)

    if is_valid_queryparam(amount_max):
        queryset = queryset.filter(amount__lte=amount_max)

    return queryset
