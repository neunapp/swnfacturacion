from django import forms
from .models import Provider, Invoice, Invoice_Detail


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            'ruc',
            'razon_social',
            'address',
        ]
        labels ={
            'ruc': 'numero de ruc',
            'razon_social': 'nombre de la empresa',
            'address' : 'direccion',
        }
        widgets = {
            'ruc': forms.TextInput(attrs={'class':'form-control'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'serie',
            'numero',
            'date',
            'amount',
        ]
        labels = {
            'serie': 'serie de factura',
            'numero': 'numero de factura',
            'date': 'fecha de factura',
            'amount': 'monto de factura',
            #'igv' : 'igv',
        }
        widgets = {
            'serie': forms.TextInput(attrs={'class':'form-control'}),
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'amount': forms.TextInput(attrs={'class':'form-control'}),
            #'igv': forms.TextInput(attrs={'class':'form-control'}),
        }

class Invoice_DetailForm(forms.ModelForm):

    class Meta:
        model = Invoice_Detail
        fields = [
            'service',
            'description',
        ]
        labels = {
            'service': 'servicio',
            'description': 'descripcion del servicio',
        }
        widgets={
            'service': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }

class ReportForm(forms.Form):

    date_start = forms.DateField()
    date_end = forms.DateField()
    search = forms.CharField()

    def clean_date_end(self):
        inicio = self.cleaned_data['date_start']
        fin = self.cleaned_data['date_end']

        if(inicio > fin):
            mensaje = 'La fecha inicio no puede ser mayor a la fecha fin'
            self.add_error('date_end',mensaje)
        else:
            return fin


class ProviderUpdateForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            'ruc',
            'razon_social',
            'address',
        ]
        labels ={
            'ruc': 'numero de ruc',
            'razon_social': 'nombre de la empresa',
            'address' : 'direccion',
        }
        widgets = {
            'ruc': forms.TextInput(attrs={'class':'form-control'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'anulate',
        ]

class Invoice_DetailUpdateForm(forms.ModelForm):

    class Meta:
        model = Invoice_Detail
        fields = [
            'service',
            'description',
        ]
        labels = {
            'service': 'servicio',
            'description': 'descripcion del servicio',
        }
        widgets={
            'service': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }
