from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from datetime import date, timedelta
from .models import Ong, PLAN_TYPES


@receiver(user_logged_in)
def check_premium_plans(sender, user, request, **kwargs):
    # Buscamos todas las ONG con plan Premium y fecha de pago anterior a hace un mes
    one_month_ago = date.today() - timedelta(days=30)
    outdated_ongs = Ong.objects.filter(plan=PLAN_TYPES[1][0],
                                       premium_payment_date__lte=one_month_ago)

    # Actualizamos el plan a Básico y eliminamos la fecha de pago premium
    for ong in outdated_ongs:
        ong.plan = PLAN_TYPES[0][0]
        ong.premium_payment_date = None
        ong.save()
