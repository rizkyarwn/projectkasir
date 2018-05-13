from django import template
from django.utils import timezone
from django.db.models import Sum
from app_kasir.models import (Produk, Transaksi, DetailTransaksi)


register = template.Library()


@register.filter
def get_total_transaksi_this_month(month):
	#detail_transaksi = DetailTransaksi.objects\
	#	.filter(transaksi__tanggal_transaksi__month=month)\
	#	.annotate(total=Sum('produk__harga')).order_by('-total')
	#print(detail_transaksi)
	#return detail_transaksi
	return Transaksi.objects.filter(tanggal_transaksi__month=month).count()

@register.filter
def get_total_harga_this_day(hour):
	return Transaksi.objects.filter(
		tanggal_transaksi__day=timezone.now().day,
		tanggal_transaksi__hour=hour
		).count()

@register.filter
def get_total_produk_this_month():
	return DetailTransaksi.objects.filter(total_transaksi__month=month).count()

#popular makanan
@register.filter
def get_popular_makanan():
	mapping = [
		{
		'produk_name': produk,
		'total_saled_makanan': DetailTransaksi.objects.filter(produk=produk).count()
		} for produk in Produk.objects.all()
	]
	mapping.sort(key=lambda x: int(x['total_saled_makanan']), reverse=True)
	return mapping[:5]
	#return mapping

#popular minuman
@register.filter
def get_popular_minuman():
	mapping = [
		{
		'produk_name': produk.objects.filter(tipe='minuman'),
		'total_saled_minuman': DetailTransaksi.objects.filter(produk=produk).count()
		} for produk in Produk.objects.all()
	]
	mapping.sort(key=lambda x: int(x['total_saled_minuman']), reverse=True)
	#return mapping[:5]
	return mapping