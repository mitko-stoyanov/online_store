from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clothes_shop.web.forms import AddAccessoriesForm, EditAccessoriesForm, DeleteAccessoriesForm
from clothes_shop.web.helpers import CheckUserAccessMixin
from clothes_shop.web.models import Accessories


class ShowAccessoriesShopView(ListView):
    template_name = 'accessories/accessories-shop.html'
    model = Accessories
    context_object_name = 'all_accessories'


class AccessoriesDetailView(DetailView):
    model = Accessories
    template_name = 'accessories/accessories-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class AddAccessoriesView(PermissionRequiredMixin, CreateView):
    permission_required = 'web.add_accessories'

    def handle_no_permission(self):
        return redirect('forbidden page')

    template_name = 'accessories/add-accessories.html'
    form_class = AddAccessoriesForm
    success_url = reverse_lazy('accessories shop')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditAccessoriesView(LoginRequiredMixin, CheckUserAccessMixin, UpdateView):
    model = Accessories
    template_name = 'accessories/edit-accessories.html'
    form_class = EditAccessoriesForm

    def get_success_url(self):
        return reverse_lazy('accessories-shop single', kwargs={'pk': self.object.id})


class DeleteAccessoryView(PermissionRequiredMixin, LoginRequiredMixin, CheckUserAccessMixin, DeleteView):
    permission_required = 'web.delete_accessories'

    model = Accessories
    template_name = 'accessories/accessories-delete.html'
    form_class = DeleteAccessoriesForm
    success_url = reverse_lazy('accessories shop')
