from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from clothes_shop.web.forms import EditClothesForm, DeleteClothesForm, AddClothesForm
from clothes_shop.web.helpers import CheckUserAccessMixin
from clothes_shop.web.models import Clothes


class ShowClothesShopView(ListView):
    template_name = 'clothes/clothes-shop.html'
    model = Clothes
    context_object_name = 'all_clothes'


class ClothesDetailView(DetailView):
    model = Clothes
    template_name = 'clothes/shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditClothesView(LoginRequiredMixin, CheckUserAccessMixin, UpdateView):
    model = Clothes
    template_name = 'clothes/edit-clothes.html'
    form_class = EditClothesForm

    def get_success_url(self):
        return reverse_lazy('shop single', kwargs={'pk': self.object.id})


class DeleteClothesView(PermissionRequiredMixin, LoginRequiredMixin, CheckUserAccessMixin, DeleteView):
    permission_required = 'web.delete_clothes'

    model = Clothes
    template_name = 'clothes/delete-clothes.html'
    form_class = DeleteClothesForm
    success_url = reverse_lazy('clothes shop')


class AddClothesView(PermissionRequiredMixin, CreateView):
    permission_required = 'web.add_clothes'

    def handle_no_permission(self):
        return redirect('forbidden page')

    template_name = 'clothes/add-clothes.html'
    form_class = AddClothesForm
    success_url = reverse_lazy('clothes shop')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
