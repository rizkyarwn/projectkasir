from django.conf.urls import url

from app_kasir.views import *

urlpatterns = [
    url(r'^$', homepage, name='home_page'),
    url(r'^order/add/(?P<meja_id>[\d-]+)/$', add_order, name='add_order_page'),
    url(r'^pelanggan/add/$', add_pelanggan, name='add_pelanggan_page'),
    url(r'^product/view/$', view_produk, name='view_produk_page'),
    url(r'^product/add/$', add_produk, name='add_produk_page'),
    url(r'^product/order/$', view_order, name='view_order_page'),
    url(r'^product/order/update/(?P<pk>[\d-]+)/$', update_order, name='update_order_page'),
    url(r'^product/data_tf/(?P<order_id>[\d-]+)/$', add_transaksi, name='add_data_transaksi'),
    url(r'^product/transaksi/$', view_transaksi, name='view_transaksi_page'),
    url(r'^statistik/view/$', view_statistik, name='view_statistik'),

    url(r'^product/detail_transaksi/(?P<pk>[\d-]+)/$', view_detail_transaksi, name='view_detail_transaksi_page'),
    url(r'^product/detail_order/(?P<pk>[\d-]+)/$', view_detail_order, name='view_detail_order_page'),
    url(r'^product/order/delete/(?P<pk>[\d-]+)/$', delete_order, name='delete_order_page'),
    url(r'^product/update/(?P<produk_id>[\d-]+)/$', update_produk, name='update_produk_page'),
    url(r'^product/delete/(?P<produk_id>[\d-]+)/$', delete_produk, name='delete_produk_page'),
    url(r'^product/search/json/$', search_json_produk, name='search_json_produk_page'),
]