from django.urls import path

from clothes_shop.web.views.accessories_views import ShowAccessoriesShopView, AccessoriesDetailView, AddAccessoriesView, \
    EditAccessoriesView, DeleteAccessoryView
from clothes_shop.web.views.authentication_views import UserRegistrationView, UserLoginView, UerLogoutView, \
    ChangePasswordView, DeleteProfileView
from clothes_shop.web.views.clothes_views import ShowClothesShopView, ClothesDetailView, AddClothesView, \
    EditClothesView, DeleteClothesView
from clothes_shop.web.views.main_views import show_index, show_about, ContactView, show_profile, MessagesListView, \
    DeleteMessage, show_product_category, show_my_adds, show_all_adds, show_forbidden_page
from clothes_shop.web.views.shoes_views import ShowShoesShopView, ShoesDetailView, EditShoesView, DeleteShoesView, \
    AddShoesView

urlpatterns = (
    # ------------------------- general urls -------------------------
    path('', show_index, name='index'),
    path('about/', show_about, name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('add/', show_product_category, name='add products'),

    # ------------------------- authentication urls -------------------------
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UerLogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),

    # ------------------------- shops urls -------------------------
    path('clothes-shop/', ShowClothesShopView.as_view(), name='clothes shop'),
    path('shoes-shop/', ShowShoesShopView.as_view(), name='shoes shop'),
    path('accessories-shop/', ShowAccessoriesShopView.as_view(), name='accessories shop'),

    # ------------------------- clothes shop urls -------------------------
    path('shop/single/<int:pk>/', ClothesDetailView.as_view(), name='shop single'),
    path('add/clothes/', AddClothesView.as_view(), name='add_clothing'),
    path('edit/clothes/<int:pk>', EditClothesView.as_view(), name='edit_clothing'),
    path('delete/clothes/<int:pk>', DeleteClothesView.as_view(), name='delete_clothing'),

    # ------------------------- shoes shop urls -------------------------
    path('shoes-shop/single/<int:pk>/', ShoesDetailView.as_view(), name='shoes-shop single'),
    path('edit/shoes/<int:pk>', EditShoesView.as_view(), name='edit_shoes'),
    path('delete/shoes/<int:pk>', DeleteShoesView.as_view(), name='delete_shoes'),
    path('add/shoes/', AddShoesView.as_view(), name='add_shoes'),

    # ------------------------- accessories shop urls -------------------------
    path('accessories-shop/single/<int:pk>/', AccessoriesDetailView.as_view(), name='accessories-shop single'),
    path('add/accessories/', AddAccessoriesView.as_view(), name='add_accessories'),
    path('edit/accessories/<int:pk>', EditAccessoriesView.as_view(), name='edit_accessories'),
    path('delete/accessories/<int:pk>', DeleteAccessoryView.as_view(), name='delete_accessories'),

    # ------------------------- profile urls -------------------------
    path('profile/', show_profile, name='profile'),
    path('profile/messages/', MessagesListView.as_view(), name='messages'),
    path('profile/messages/delete/<int:pk>/', DeleteMessage.as_view(), name='delete_message'),
    path('profile/my-adds/', show_my_adds, name='my adds'),
    path('profile/all/', show_all_adds, name='all adds'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),

    # ------------------------- error pages -------------------------
    path('forbidden/', show_forbidden_page, name='forbidden page')
)
