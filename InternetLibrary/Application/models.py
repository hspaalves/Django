from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):

    id = models.AutoField(_('id'), primary_key=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    summary = models.CharField(_('summary'), max_length=300, blank=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return " %s " % (
            self.name
        )


class Author(models.Model):
    id = models.AutoField(_('id'), primary_key=True)
    name = models.CharField(_('name'), max_length=50, blank=True)
    book = models.ManyToManyField(Book)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return "%s | %s | %s" % (
            self.name,
            self.id,
            self.book
        )
