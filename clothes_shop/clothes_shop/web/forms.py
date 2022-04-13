from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import Group

from clothes_shop.web.helpers import BootstrapFormMixin
from clothes_shop.web.models import Contact, Clothes, Shoes, Accessories

UserModel = get_user_model()


# ------------------------- Authentication forms -------------------------

class UserRegistrationForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        group = Group.objects.get(name='regular_user')
        user.groups.add(group)

        if commit:
            user.save()
        return user


class UserLoginForm(BootstrapFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class ChangePasswordForm(BootstrapFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class ContactForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter a full name'},
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Enter a valid email'},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


# ------------------------- Clothe forms -------------------------


class AddClothesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ('title', 'brand', 'clothes_type', 'materials', 'description', 'image', 'price')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter a title'},
            ),
            'brand': forms.TextInput(
                attrs={'placeholder': 'Enter a brand(Not Required)'},
            ),
            'materials': forms.TextInput(
                attrs={'placeholder': 'Enter a materials'},
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter a description'},
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        clothing = super().save(commit=False)
        clothing.user = self.user
        if commit:
            clothing.save()
        return clothing


class EditClothesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ('title', 'brand', 'clothes_type', 'materials', 'description', 'image', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class DeleteClothesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ('title', 'brand', 'clothes_type', 'materials', 'description', 'image', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


# ------------------------- Shoe forms -------------------------


class AddShoesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ('title', 'size', 'price', 'shoes_type', 'suitable_for', 'description', 'image')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter a title'},
            ),
            'size': forms.TextInput(
                attrs={'placeholder': 'Enter a brand(Not Required)'},
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter a description'},
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        shoe = super().save(commit=False)
        shoe.user = self.user
        if commit:
            shoe.save()
        return shoe


class EditShoesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ('title', 'size', 'price', 'shoes_type', 'suitable_for', 'description', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class DeleteShoesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ('title', 'size', 'price', 'shoes_type', 'suitable_for', 'description', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


# ------------------------- Accessory forms -------------------------

class AddAccessoriesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ('title', 'description', 'image', 'price', 'accessories_type', 'gender')

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter a title'},
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        accessory = super().save(commit=False)
        accessory.user = self.user
        if commit:
            accessory.save()
        return accessory


class EditAccessoriesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ('title', 'description', 'image', 'price', 'accessories_type', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class DeleteAccessoriesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ('title', 'description', 'image', 'price', 'accessories_type', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
