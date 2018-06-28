from django.db import models
from django.contrib.auth.models import User


class ProdukManager(models.QuerySet):

    def published(self):
        return self.filter(ditampilkan=True)


# """ NAMA WARUNG """
# class NamaWa(object):
#     """docstring for NamaWa"""
#     nama = models.CharField(max_length=50)
#     alamat = models.TextField()
#     telp = models.IntegerField()
#     teks = models.TextField()

#     def __init__(self, arg):
#         super(NamaWa, self).__init__()
#         self.arg = arg
""" PROFIL WARUNG """
class ProfilWarung(models.Model):
    nama = models.CharField(max_length=100)
    telp = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return self.nama


""" PRODUK """
class Produk(models.Model):
    author = models.ForeignKey(User, related_name='author_product')
    PILIHAN_TIPE = (
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman'),
    )
    tipe = models.CharField(max_length=10,
                            choices=PILIHAN_TIPE)
    nama = models.CharField(max_length=50)
    harga = models.IntegerField()
    info = models.TextField()

    ditampilkan = models.BooleanField(default=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_dimodifikasi = models.DateTimeField(auto_now=True)

    objects = ProdukManager.as_manager()

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['-tanggal_dibuat']


""" MEJA PESAN """
class MejaPesan(models.Model):
    nomor = models.IntegerField(unique=True)
    PILIHAN_FASILITAS = (
        ('duduk', 'Duduk'),
        ('lesehan', 'Lesehan'),
    )
    fasilitas = models.CharField(max_length=20,
                                 choices=PILIHAN_FASILITAS)
    #dipesan = models.BooleanField(default=False)

    def __str__(self):
        return 'meja nomor: %s' % self.nomor

    class Meta:
        ordering = ['nomor']

""" PELANGGAN """
class Pelanggan(models.Model):
    nama = models.CharField(max_length=50)
    meja = models.ForeignKey(MejaPesan)

    def __str__(self):
        return self.nama


""" ORDER/PESANAN """
class Order(models.Model):
    pelanggan = models.ForeignKey(Pelanggan)
    tanggal_order = models.DateTimeField(auto_now_add=True)

    @property
    def total_order(self):
        beli = DetailOrder.objects.filter(order=self.pk)
        t = 0
        for b in beli:
            t += b.produk.harga * b.qty * (1-b.diskon)
        return t

    def get_detail_orders(self):
        return DetailOrder.objects.filter(order=self)

    def __str__(self):
        return '%s' % (self.pelanggan)

    class Meta:
        ordering = ['-tanggal_order']


""" DETAIL ORDER/PESANAN """
class DetailOrder(models.Model):
    order = models.ForeignKey(Order)
    produk = models.ForeignKey(Produk)
    qty = models.PositiveIntegerField(default=1)
    diskon = models.FloatField(default=0.0)

    @property
    def total_harga_produk(self):
        return self.produk.harga * self.qty

    def __str__(self):
        return '%s %s' % (self.order, self.produk)


""" TRANSAKSI/PEMBAYARAN """
class Transaksi(models.Model):
    pelanggan = models.ForeignKey(Pelanggan)
    tanggal_transaksi = models.DateTimeField(auto_now_add=True)
    tanggal_order = models.DateTimeField()

    @property
    def total_transaksi(self):
        beli = DetailTransaksi.objects.filter(transaksi=self.pk)
        t = 0
        for b in beli:
            t += b.produk.harga * b.qty * (1-b.diskon)
        return t

    def __str__(self):
        return '%s' % (self.pelanggan)

    class Meta:
        ordering = ['-tanggal_transaksi']


""" DETAIL TRANSAKSI/PEMBAYARAN """
class DetailTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi)
    produk = models.ForeignKey(Produk)
    qty = models.PositiveIntegerField(default=1)
    diskon = models.FloatField(default=0.0)

    @property
    def total_harga_produk(self):
        return self.produk.harga * self.qty

    def __str__(self):
        return '%s %s' % (self.transaksi, self.produk)


