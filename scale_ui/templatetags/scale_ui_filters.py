import re

from django import template


register = template.Library()

@register.filter(name='format_float')
def format_float(value, fmt='%.2f'):
    re_digits_nondigits = re.compile(r'\d+|\D+')
    parts = re_digits_nondigits.findall(fmt % (value,))
    for i in xrange(len(parts)):
        s = parts[i]
        if s.isdigit():
            parts[i] = _commafy(s)
            break
    return ''.join(parts)
    
def _commafy(s):
    r = []
    for i, c in enumerate(reversed(s)):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    return ''.join(r)