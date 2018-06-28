from django import template
from django.utils import timezone
from django.db.models import Sum
from app_kasir.models import (Produk, Transaksi, DetailTransaksi)


register = template.Library()


@register.filter
def as_rupiah(uang):
    """
    return a number as rupiah.
    eg: 2000000 => 2.000.000
    """
    if uang is None:
        return 'Rp. 0'
    return 'Rp. {0:,}'.format(uang).replace(',', '.')


@register.filter
def get_total_transaksi_this_month(month):
	return Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year,
		tanggal_transaksi__month=month
	).count()


@register.filter
def get_total_income_this_month(month):
	return Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year,
		tanggal_transaksi__month=month
	).count()

@register.filter
def get_total_income_this_month_1(month):
	transaksi = Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year,
		tanggal_transaksi__month=month)
	total_income = [t.total_transaksi for t in transaksi]
	return sum(total_income)


@register.simple_tag
def total_income_today():
	transaksi = Transaksi.objects.filter(
		tanggal_transaksi__date=timezone.now())
	total_income = [t.total_transaksi for t in transaksi]
	return as_rupiah(sum(total_income))


@register.simple_tag
def total_income_month():
	transaksi = Transaksi.objects.filter(
		tanggal_transaksi__month=timezone.now().month,
		tanggal_transaksi__year=timezone.now().year
		)
	total_income = [t.total_transaksi for t in transaksi]
	return as_rupiah(sum(total_income))

@register.simple_tag
def total_income_year():
	transaksi = Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year
		)
	total_income = [t.total_transaksi for t in transaksi]
	return as_rupiah(sum(total_income))
	
# @register.filter
# def get_total_harga_this_week(hour):
# 	return Transaksi.objects.filter(
# 		tanggal_transaksi__year=timezone.now().year,
# 		tanggal_transaksi__day=timezone.now().day,
# 		tanggal_transaksi__hour=hour
# 	).count()
	
@register.filter
def get_total_harga_this_day(hour):
	return Transaksi.objects.filter(
		tanggal_transaksi__day=timezone.now().day,
		tanggal_transaksi__hour=hour
		).count()

@register.filter
def get_total_harga_this_day(hour):
	return Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year,
		tanggal_transaksi__day=timezone.now().day,
		tanggal_transaksi__hour=hour
	).count()

# #popular makanan
# @register.filter
# def get_popular_makanan():
# 	mapping = [
# 		{
# 		'produk_name': produk,
# 		'total_saled_makanan': DetailTransaksi.objects.filter(produk=produk).count()
# 		} for produk in Produk.objects.all()
# 	]
# 	mapping.sort(key=lambda x: int(x['total_saled_makanan']), reverse=True)
# 	return mapping[:5]
# 	#return mapping


# #popular minuman
# @register.filter
# def get_popular_minuman():
# 	mapping = [
# 		{
# 		'produk_name': produk.objects.filter(tipe='minuman'),
# 		'total_saled_minuman': DetailTransaksi.objects.filter(produk=produk).count()
# 		} for produk in Produk.objects.all()
# 	]
# 	mapping.sort(key=lambda x: int(x['total_saled_minuman']), reverse=True)
# 	return mapping[:5]
# 	# return mapping


@register.simple_tag
def transaksi_tahun_ini():
	"""
	used in: app_kasir/statistik.html
	"""
	return Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year
	).count()


@register.simple_tag
def transaksi_bulan_ini():
	"""
	used in: app_kasir/statistik.html
	"""
	return Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year,
		tanggal_transaksi__month=timezone.now().month
	).count()


@register.simple_tag
def transaksi_hari_ini():
	"""
	used in: app_kasir/statistik.html
	"""
	return Transaksi.objects.filter(
		tanggal_transaksi__year=timezone.now().year,
		tanggal_transaksi__month=timezone.now().month,
		tanggal_transaksi__day=timezone.now().day
	).count()
