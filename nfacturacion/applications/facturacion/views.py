from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, DetailView, FormView, CreateView, ListView, DeleteView, UpdateView
from .models import Provider, Invoice, Invoice_Detail

from .forms import InvoiceForm, ProviderForm, Invoice_DetailForm, ReportForm
from .forms import InvoiceUpdateForm, ProviderUpdateForm, Invoice_DetailUpdateForm

from decimal import Decimal

from datetime import datetime, date, timedelta

# Create your views here.
class ReportListView(ListView):
    context_object_name = 'lista_de_factura'
    template_name = 'facturacion/reportefacturacion.html'
    queryset = Invoice_Detail.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReportListView, self).get_context_data(**kwargs)
        context['form'] = ReportForm
        return context

    def get_queryset(self):
        a = self.request.GET.get("date_start")
        b = self.request.GET.get("date_end")
        q = self.request.GET.get("search",'')
        queryset = Invoice_Detail.objects.filter(
            invoice__numero__icontains=q,
            invoice__date__range=(a, b),
        )
        return queryset

class FacturacionCreate(CreateView):
    template_name = 'facturacion/facturacionform.html'
    model = Invoice_Detail
    form_class = Invoice_DetailForm
    second_form_class = InvoiceForm
    third_form_class = ProviderForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(FacturacionCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            print context['form2']
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid:
            invoice_detail = form.save(commit=False)
            invoice_detail.invoice = form2.save(commit=False)
            invoice_detail.invoice.igv=invoice_detail.invoice.amount * Decimal(0.180)
            invoice_detail.invoice.provider = form3.save()
            invoice_detail.invoice = form2.save()
            invoice_detail = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

            #return self.render_to_response(self.get_context_data(form=form, form2=form2))

class FacturacionUpdateView(UpdateView):
    model = Invoice
    second_model = Provider
    third_model = Invoice_Detail
    template_name = 'facturacion/index.html'
    form_class = InvoiceUpdateForm
    second_form_class = ProviderUpdateForm
    third_form_class = Invoice_DetailUpdateForm
    success_url = reverse_lazy('facturacion_app:reporte')

    def get_context_data(self, **kwargs):
        context = super(FacturacionUpdateView,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        invoice = self.model.objects.get(id=pk)
        provider = self.second_model.objects.get(id=invoice.provider.pk)
        invoice_detail = self.third_model.objects.get(id=invoice.pk)

        if 'form' not in context:
            context['form']=self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=provider)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=invoice_detail)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_invoice = self.object.pk

        invoice = self.model.objects.get(id=id_invoice)
        provider = self.second_model.objects.get(id=invoice.provider.pk)
        invoice_detail = self.third_model.objects.get(id=invoice.pk)

        form = self.form_class(request.POST, instance = invoice)
        form2 = self.second_form_class(request.POST, instance = provider)
        form3 = self.third_form_class(request.POST, instance = invoice_detail)

        if form.is_valid() and form2.is_valid() and form3.is_valid():
            print '=========2========='
            form2.save()
            form.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
