from django import template
from django.utils import timezone
from app_kasir.models import (Produk, DetailTransaksi)

register = template.Library()


@register.assignment_tag
def populartags():
    """
    {% load popular_tags %}

    {% populartags as populartags_ul %}
    {% for popular_item in populartags_ul %}
      {{ popular_item.produk_name }}
      {{ popular_item.total_saled }}
    {% endfor %}
    """
    mapping = [
        {
            'produk_name': produk,
            'total_saled': DetailTransaksi.objects.filter(produk=produk).count()
        } for produk in Produk.objects.all()
    ]
    mapping.sort(key=lambda x: int(x['total_saled']), reverse=True)
    return mapping[:5]


@register.assignment_tag
def popminuman():
    mapping = [
        {
            'produk_name': produk,
            'total_saled': DetailTransaksi.objects.filter(produk=produk, produk__tipe='minuman').count()
        } for produk in Produk.objects.all()
    ]
    mapping.sort(key=lambda x: int(x['total_saled']), reverse=True)
    return mapping[:5]


@register.assignment_tag
def popmakanan():
    mapping = [
        {
            'produk_name': produk,
            'total_saled': DetailTransaksi.objects.filter(produk=produk, produk__tipe='makanan').count()
        } for produk in Produk.objects.all()
    ]
    mapping.sort(key=lambda x: int(x['total_saled']), reverse=True)
    return mapping[:5]