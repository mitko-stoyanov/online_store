from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from clothes_shop.web.managers import AppUsersManager
from clothes_shop.web.validators import validate_only_letters


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Contact(models.Model):
    NAME_MAX_LEN = 20
    SUBJECT_MAX_LEN = 25

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=SUBJECT_MAX_LEN,
    )

    message = models.TextField()

    def __str__(self):
        return f'{self.name} -> {self.subject}'


class Clothes(models.Model):
    TITLE_MAX_LEN = 30

    BRAND_MAX_LEN = 20

    MATERIALS_MAX_LEN = 25

    T_SHIRTS = 'T-Shirts'
    JEANS = 'Jeans'
    UNDERWEAR = 'Underwear'
    SHORTS = 'Shorts'
    HOODIES = 'Hoodies'

    PRICE_MIN_VALUE = 0

    TYPES = [(x, x) for x in (T_SHIRTS, JEANS, UNDERWEAR, SHORTS, HOODIES)]

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(
            validate_only_letters,
        )
    )

    brand = models.CharField(
        max_length=BRAND_MAX_LEN,
        null=True,
        blank=True,
    )

    clothes_type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
        default=T_SHIRTS,
    )

    materials = models.CharField(
        max_length=MATERIALS_MAX_LEN,
    )

    description = models.TextField()

    image = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Clothes'

    def __str__(self):
        return f'{self.title} -> {self.price:.2f}'


class Shoes(models.Model):
    TITLE_MAX_LEN = 30

    MIN_PRICE_VALUE = 0

    SNEAKERS = 'Sneakers'
    SANDALS = 'Sandals'
    HIGH_HEELS = 'High Heels'
    FLIP_FLOPS = 'Flip Flops'
    RUNNING_SHOES = 'Running Shoes'

    SUMMER = 'Summer'
    AUTUMN = 'Autumn'
    WINTER = 'Winter'
    SPRING = 'Spring'

    TYPES = [(x, x) for x in (SNEAKERS, SANDALS, HIGH_HEELS, FLIP_FLOPS, RUNNING_SHOES)]

    SEASON_TYPE = [(y, y) for y in (SUMMER, AUTUMN, WINTER, SPRING)]

    SIZE_MIN_VALUE = 2
    SIZE_MAX_VALUE = 12

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(
            validate_only_letters,
        )
    )

    size = models.IntegerField(
        validators=(
            MinValueValidator(SIZE_MIN_VALUE),
            MaxValueValidator(SIZE_MAX_VALUE),
        )
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE_VALUE),
        )
    )

    shoes_type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
        default=SNEAKERS,
    )

    suitable_for = models.CharField(
        max_length=max(len(x) for x, _ in SEASON_TYPE),
        choices=SEASON_TYPE,
        default=SUMMER,
    )

    description = models.TextField()

    image = models.URLField()

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return f'{self.title} -> {self.price:.2f}'


class Accessories(models.Model):
    TITLE_MAX_LEN = 30

    PRICE_MIN_VALUE = 0

    SUNGLASSES = 'Sunglasses'
    WATCHES = 'Watches'
    BRACELET = 'Bracelet'
    HAT = 'Hat'

    TYPES = [(x, x) for x in (SUNGLASSES, WATCHES, BRACELET, HAT)]

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(g, g) for g in (MALE, FEMALE, DO_NOT_SHOW)]

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(
            validate_only_letters,
        )
    )

    description = models.TextField()

    image = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    accessories_type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
        default=HAT,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Accessories'

    def __str__(self):
        return f'{self.title} -> {self.price:.2f}'
