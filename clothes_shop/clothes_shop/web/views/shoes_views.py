from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clothes_shop.web.forms import AddShoesForm, EditShoesForm, DeleteShoesForm
from clothes_shop.web.helpers import CheckUserAccessMixin
from clothes_shop.web.models import Shoes


class ShowShoesShopView(ListView):
    template_name = 'shoes/shoes-shop.html'
    model = Shoes
    context_object_name = 'all_shoes'


class ShoesDetailView(DetailView):
    model = Shoes
    template_name = 'shoes/shoes-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class AddShoesView(PermissionRequiredMixin, CreateView):
    permission_required = 'web.add_clothes'

    def handle_no_permission(self):
        return redirect('forbidden page')

    template_name = 'shoes/add-shoes.html'
    form_class = AddShoesForm
    success_url = reverse_lazy('shoes shop')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditShoesView(LoginRequiredMixin, CheckUserAccessMixin, UpdateView):
    model = Shoes
    template_name = 'shoes/edit-shoes.html'
    form_class = EditShoesForm

    def get_success_url(self):
        return reverse_lazy('shoes-shop single', kwargs={'pk': self.object.id})


class DeleteShoesView(PermissionRequiredMixin, LoginRequiredMixin, CheckUserAccessMixin, DeleteView):
    permission_required = 'web.delete_shoes'

    def handle_no_permission(self):
        return redirect('forbidden page')

    model = Shoes
    template_name = 'shoes/shoes-delete.html'
    form_class = DeleteShoesForm
    success_url = reverse_lazy('shoes shop')
