from django.db import models


class Sample(models.Model):

    def __repr__(self):
        return "{}. ".format(self.pk)

    __str__ = __repr__
