from django.contrib import admin

from app_kasir.models import Produk, MejaPesan, Pelanggan, Order, DetailOrder, Transaksi, DetailTransaksi

class PelangganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'meja')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pelanggan', 'tanggal_order', 'total_order')

class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('pelanggan', 'tanggal_transaksi', 'total_transaksi')

class DetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'produk', 'qty', 'diskon')

class DetailtfAdmin(admin.ModelAdmin):
    list_display = ('transaksi', 'produk', 'qty', 'diskon')

class MejaAdmin(admin.ModelAdmin):
    list_display = ('nomor', 'fasilitas')

admin.site.register(Produk)
admin.site.register(MejaPesan, MejaAdmin)
admin.site.register(Pelanggan, PelangganAdmin)

admin.site.register(Order, OrderAdmin)
admin.site.register(Transaksi, TransaksiAdmin)

admin.site.register(DetailOrder, DetailAdmin)
admin.site.register(DetailTransaksi, DetailtfAdmin)