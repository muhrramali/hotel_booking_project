from django import template
register = template.Library()

@register.filter
def has_payment(reservation):
    try:
        return reservation.payment is not None
    except Exception:
        return False
