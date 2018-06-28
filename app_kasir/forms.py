from django import forms
from app_kasir.models import Produk, Pelanggan, Order


class ProdukForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProdukForm, self).__init__(*args, **kwargs)
		self.fields['tipe'].widget.attrs = {'class' : 'form-control'}
		self.fields['nama'].widget.attrs = {'class' : 'form-control'}
		self.fields['harga'].widget.attrs = {'class' : 'form-control'}
		self.fields['info'].widget.attrs = {'class' : 'form-control'}
		# self.fields['info'].widget.attrs = {'class' : 'form-control', 'style' : 'width : 300px;'}
		
	class Meta:
		model = Produk
		fields = '__all__'
		exclude = ['author', 'tanggal_dibuat', 'tanggal_dimodifikasi']

class PelangganForm(forms.ModelForm):
	class Meta:
		model = Pelanggan
		fields = '__all__'