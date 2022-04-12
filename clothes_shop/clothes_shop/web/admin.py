from django.contrib import admin

from clothes_shop.web.models import Contact, Clothes, AppUser, Shoes, Accessories


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    pass


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    pass
