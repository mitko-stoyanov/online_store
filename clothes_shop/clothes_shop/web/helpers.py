from django.shortcuts import redirect


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class CheckUserAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser and \
                not request.user.pk == self.kwargs['pk']:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class ProfileDataMixin:
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '12345',
    }


class ClothesDataMixin:
    VALID_CLOTHES_CREDENTIALS = {
        'title': 'MyClothes',
        'clothes_type': 'Jeans',
        'materials': 'Cotton',
        'description': 'dasdasd',
        'image': 'http://cat.png',
        'price': 143,
    }


class ShoesDataMixin:
    VALID_SHOES_DATA = {
        'title': 'NewShoes',
        'size': 4,
        'price': 134,
        'shoes_type': 'Sandals',
        'suitable_for': 'Summer',
        'description': 'dsadas',
        'image': 'https://shoes.png',
    }


class AccessoriesDataMixin:
    VALID_ACCESSORIES_DATA = {
        'title': 'NewAccessories',
        'description': 'dasdas',
        'image': 'https://accessories.png',
        'price': 150,
        'accessories_type': 'Sunglasses',
        'gender': 'Male',
    }
