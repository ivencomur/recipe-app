from django import template
from fractions import Fraction
from decimal import Decimal
register = template.Library()

@register.filter
def pretty_qty(q):
    if q is None: 
        return ""
    try:
        q = Decimal(q)
    except Exception:
        return ""
    if q == 0:
        return ""
    frac = Fraction(q).limit_denominator(8)
    n, d = frac.numerator, frac.denominator
    whole, rem = divmod(n, d)
    if whole and rem:
        return f"{whole} " + _frac_unicode(rem, d)
    if whole:
        return str(whole)
    return _frac_unicode(n, d)

def _frac_unicode(n, d):
    m = {(1,2):"½",(1,3):"⅓",(2,3):"⅔",(1,4):"¼",(3,4):"¾",(1,5):"⅕",(2,5):"⅖",(3,5):"⅗",(4,5):"⅘",(1,6):"⅙",(5,6):"⅚",(1,8):"⅛",(3,8):"⅜",(5,8):"⅝",(7,8):"⅞"}
    return m.get((n,d), f"{n}/{d}")

@register.filter
def ingredient_line(ri):
    name = getattr(getattr(ri, "ingredient", None), "name", "") or "Ingredient"
    qty  = pretty_qty(getattr(ri, "quantity", None))
    unit = (getattr(ri, "unit", "") or "").strip()
    return (f"{name}: {qty} {unit}".strip() if qty else name)
