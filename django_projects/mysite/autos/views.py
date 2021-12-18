from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

from autos.models import Make, Auto
from autos.forms import MakeForm


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count()
        auto_list = Auto.objects.all()

        ctx = {'auto_list': auto_list, 'make_count': make_count}
        return render(request, 'autos/auto_list.html', context=ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', context=ctx)


class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        frm = MakeForm()
        ctx = {'form': frm}
        return render(request, self.template, context=ctx)

    def post(self, request):
        frm = MakeForm(request.POST)
        if not frm.is_valid():
            ctx = {'form': frm}
            return render(request, self.template, context=ctx)

        make = frm.save()
        return redirect(self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request, pk):
        make = get_object_or_404(model=self.model, pk=pk)
        frm = MakeForm(instance=make)
        ctx = {'form': frm}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(model=self.model, pk=pk)
        frm = MakeForm(request.POST, instance=make)

        if not frm.is_valid():
            ctx = {'form': frm}
            return render(request, self.template, ctx)

        frm.save()
        return redirect(self.success_url)


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
