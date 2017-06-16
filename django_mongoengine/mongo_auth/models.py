from bson.objectid import ObjectId
from .managers import MongoUserManager
from django.db import models

from .auth import make_password, BaseUser


class MongoUser(BaseUser, models.Model):
    """"
    Dummy user model for Django.

    MongoUser is used to replace Django's UserManager with MongoUserManager.
    The actual user document class is django_mongoengine.auth.models.User or any
    other document class specified in MONGOENGINE_USER_DOCUMENT.

    To get the user document class, use `get_user_document()`.
    """

    objects = MongoUserManager()

    class Meta:
        app_label = 'mongo_auth'

    def set_password(self, password):
        """Doesn't do anything, but works around the issue with Django 1.6."""
        make_password(password)

MongoUser._meta.pk.to_python = ObjectId
