import unicodedata

from django.utils.functional import cached_property
from django.utils.html import escape
from django.utils.safestring import SafeData, mark_safe
from django.utils.text import normalize_newlines


def remove_accent(string_with_diacritics):
    "Removes a diacritics from a given string"
    return unicodedata.normalize('NFKD', string_with_diacritics).encode('ASCII', 'ignore').decode('ASCII')


def get_class_method(cls_or_inst, method_name):
    cls = cls_or_inst
    if not isinstance(cls, type):
        cls = cls_or_inst.__class__
    meth = getattr(cls, method_name, None)
    if isinstance(meth, property):
        meth = meth.fget
    elif isinstance(meth, cached_property):
        meth = meth.func
    return meth


def keep_spacing(value, autoescape=True):
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    value = mark_safe(value.replace('  ', ' &nbsp;'))
    return mark_safe(value.replace('\n', '<br />'))
