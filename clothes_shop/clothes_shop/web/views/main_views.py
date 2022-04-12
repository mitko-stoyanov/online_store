from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from clothes_shop.web.forms import ContactForm
from clothes_shop.web.models import Contact, Clothes, Shoes, Accessories


def show_profile(request):
    context = {
        'messages_count': Contact.objects.all().count(),
    }
    return render(request, 'profile/profile.html', context)


def show_my_adds(request):
    clothes = []
    shoes = []
    accessories = []

    if Clothes.objects.all():
        clothes = Clothes.objects.filter(user=request.user)
    if Shoes.objects.all():
        shoes = Shoes.objects.filter(user=request.user)
    if Accessories.objects.all():
        accessories = Accessories.objects.filter(user=request.user)

    context = {
        'clothes': clothes,
        'shoes': shoes,
        'accessories': accessories,
    }
    return render(request, 'profile/my-ads.html', context)


def show_all_adds(request):
    clothes = Clothes.objects.all()
    shoes = Shoes.objects.all()
    accessories = Accessories.objects.all()

    context = {
        'clothes': clothes,
        'shoes': shoes,
        'accessories': accessories,
    }
    return render(request, 'profile/all-adds.html', context)


def show_index(request):
    products = []

    if Clothes.objects.all():
        last_clothing = Clothes.objects.order_by('-id')[0:1].get()
        products.append(last_clothing)
    if Shoes.objects.all():
        last_shoes = Shoes.objects.order_by('-id')[0:1].get()
        products.append(last_shoes)
    if Accessories.objects.all():
        last_accessories = Accessories.objects.order_by('-id')[0:1].get()
        products.append(last_accessories)

    context = {
        'all_products': products,
    }
    return render(request, 'index.html', context)


class AboutPageView(TemplateView):
    template_name = 'about.html'


class AddProductsCategoryView(TemplateView):
    template_name = 'add-product.html'


class ForbiddenPageView(TemplateView):
    template_name = 'forbidden-page.html'


class ContactView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contacts/contact.html'
    success_url = reverse_lazy('index')
    form_class = ContactForm
    login_url = 'login'


class MessagesListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'web.view_contact'

    def handle_no_permission(self):
        return redirect('forbidden page')

    model = Contact
    template_name = 'contacts/messages.html'


class DeleteMessage(PermissionRequiredMixin, DeleteView):
    permission_required = 'web.delete_contact'

    def handle_no_permission(self):
        return redirect('forbidden page')

    model = Contact
    success_url = reverse_lazy('messages')
