from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from app_kasir.models import MejaPesan, Produk, Pelanggan, Order, DetailOrder, Transaksi, DetailTransaksi
from app_kasir.forms import ProdukForm, PelangganForm

@login_required
def homepage(request):
    template_name = 'app_kasir/kasir_homepage.html'
    semua_meja = MejaPesan.objects.all()
    semua_meja_duduk = semua_meja.filter(fasilitas='duduk')
    semua_meja_lesehan = semua_meja.filter(fasilitas='lesehan')
    context = {
        'semua_meja': semua_meja,
        'semua_meja_duduk': semua_meja_duduk,
        'semua_meja_lesehan': semua_meja_lesehan
    }
    return render(request, template_name, context)

""" PRODUK """
@login_required
def add_produk(request):
    template_name = 'app_kasir/kasir_produk_add.html'
    semua_produk = Produk.objects.all()
    form = ProdukForm()
    context = {'form': form, 'semua_produk': semua_produk}

    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            initial = form.save(commit=False)
            initial.author = request.user
            initial.save()
            form.save()
            return redirect('view_produk_page')
        else:
            context.update({'error_message': 'Gagal memasukkan data'})
    return render(request, template_name, context)

@login_required
def update_produk(request, produk_id):
    template_name = 'app_kasir/kasir_produk_update.html'
    produk = get_object_or_404(Produk, id=produk_id)
    form = ProdukForm(instance=produk)
    context = {'produk': produk, 'form':form}
    if request.POST:
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('view_produk_page')
        else:
            context.update({'error_message': 'Gagal memasukkan data'})
    return render(request, template_name, context)

@login_required
def delete_produk(request, produk_id):
    produk = get_object_or_404(Produk, id=produk_id)
    produk.delete()
    return redirect('view_produk_page')

def view_produk(request):
    template_name = 'app_kasir/kasir_produk_view.html'
    semua_produk = Produk.objects.all()
    semua_produk_makanan = semua_produk.filter(tipe='makanan')
    semua_produk_minuman = semua_produk.filter(tipe='minuman')
    context = {
        'semua_produk': semua_produk,
        'semua_produk_makanan': semua_produk_makanan,
        'semua_produk_minuman': semua_produk_minuman
    }
    return render(request, template_name, context)
""" CLOSE PRODUK """

""" PELANGGAN """
def add_pelanggan(request):
    template_name = 'app_kasir/kasir_pelanggan_add.html'
    form = PelangganForm(request.POST)
    context = {'form': form}

    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            initial = form.save(commit=False)
            initial.author = request.user
            initial.save()
            form.save()
            return redirect('home_page')
        else:
            context.update({'error_message': 'Gagal memasukkan data'})
    return render(request, template_name, context)
""" CLOSE PELANGGAN """

""" OREDER """
@login_required
def add_order(request, meja_id):
    template_name = 'app_kasir/kasir_page_order.html'
    meja = get_object_or_404(MejaPesan, id=meja_id)
    semua_produk = Produk.objects.published()
    context = {'semua_produk': semua_produk, 'MejaPesan': meja}

    if request.method == 'POST':
        meja = get_object_or_404(MejaPesan, pk=request.POST.get('meja_pesan'))
        nama_pelanggan = request.POST.get('nama_pelanggan')
        pelanggan = Pelanggan.objects.create(nama=nama_pelanggan, meja=meja)
        order = Order.objects.create(pelanggan=pelanggan)

        id_products = request.POST.getlist('pk')
        qty_products = request.POST.getlist('qty')

        for id_produk, jumlah in zip(id_products, qty_products):
            detail_order = DetailOrder.objects.create(
                order=order,
                produk=get_object_or_404(Produk, pk=id_produk),
                qty=jumlah
            )
            detail_order.save()
        return redirect('view_detail_order_page', pk=order.pk)
    return render(request, template_name, context)

@login_required
def update_order(request, pk):
    template_name = 'app_kasir/kasir_page_order.html'
    order = get_object_or_404(Order, pk=pk)
    context = {
        'order': order,
        'MejaPesan': order.pelanggan.meja
    }

    if request.POST:
        id_products = request.POST.getlist('pk')
        qty_products = request.POST.getlist('qty')

        for id_produk, jumlah in zip(id_products, qty_products):
            detail_order, truefalse = DetailOrder.objects.get_or_create(
                order=order,
                produk=get_object_or_404(Produk, pk=id_produk),
                qty=jumlah
            )
            detail_order.save()
        return redirect('view_detail_order_page', pk=order.pk)
    return render(request, template_name, context)

def view_order(request):
    template_name = 'app_kasir/kasir_page_order_view.html'
    semua_order = Order.objects.all()
    context = {'semua_order': semua_order}
    return render(request, template_name, context)

def view_detail_order(request, pk):
    template_name = 'app_kasir/kasir_page_detail_order.html'
    order = get_object_or_404(Order, pk=pk)
    semua_order = DetailOrder.objects.filter(order=order)
    context = {'semua_order': semua_order, "order": order}
    return render(request, template_name, context)

@login_required
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('view_order_page')

@login_required
def search_json_produk(request):
    query = request.GET.get('q')
    context = {'query': query}
    if query:
        semua_produk = Produk.objects.published()\
                             .filter(nama__icontains=query)[:10]
        data = [
            {'pk': p.pk, 'nama': p.nama, 'harga': p.harga}
            for p in semua_produk
        ]
        context.update({'data': data})
    return JsonResponse(context)
"""CLOSE ORDER"""

""" TRANSAKSI """
@login_required
def add_transaksi(request, order_id):
    template_name = 'app_kasir/kasir_page_order.html'
    order = get_object_or_404(Order, id=order_id)
    transaksi = Transaksi.objects.create(pelanggan=order.pelanggan, tanggal_order=order.tanggal_order)
    transaksi.save()

    for detail_order in order.get_detail_orders():
        detail_transaksi = DetailTransaksi.objects.create(
            transaksi=transaksi,
            #tanggal=tanggal_order.order,
            produk=detail_order.produk,
            qty=detail_order.qty,
            diskon=detail_order.diskon
        )
        detail_transaksi.save()

    order.delete()
    return redirect('view_transaksi_page')

def view_transaksi(request):
    template_name = 'app_kasir/kasir_page_transaksi_view.html'
    semua_transaksi = Transaksi.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        semua_transaksi = semua_transaksi.filter(tanggal_transaksi__range=[start_date, end_date])
    context = {'semua_transaksi': semua_transaksi}
    return render(request, template_name, context)

def view_detail_transaksi(request, pk):
    template_name = 'app_kasir/kasir_page_detail_transaksi.html'
    transaksi = get_object_or_404(Transaksi, pk=pk)
    semua_transaksi = DetailTransaksi.objects.filter(transaksi=transaksi)
    context = {'semua_transaksi': semua_transaksi, "transaksi": transaksi}
    return render(request, template_name, context)

def view_statistik(request):
    template_name = 'app_kasir/statistik.html'
    semua_transaksi = Transaksi.objects.all()
    context = {'semua_transaksi': semua_transaksi}
    return render(request, template_name, context)
""" CLOSE TRANSAKSI """