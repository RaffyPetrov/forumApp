from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from forumApp.accounts.managers import AppUserManager


class AppUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'  # USERNAME_FIELD means the first credential in our auth
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30,)
    points = models.IntegerField(default=0)


# class CustomProxyModel(CustomUser):
#
#     def custom_method(self):
#         return f"This is custom method"
#
#     class Meta:
#         proxy = True
#
# print(CustomUser.objects.all())
# print(CustomProxyModel.objects.all())
