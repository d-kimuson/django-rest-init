from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator


class ToListMixin:
    @classmethod
    def to_list(cls, base=None, **kwargs):
        base = cls.objects.all() if base is None else base
        try:
            filtered = base.filter(**kwargs)
        except AttributeError as e:
            print(e)
            filtered = []

        return [inst.to_dict() for inst in filtered]


class Sample(models.Model, ToListMixin):
    name = models.CharField(
        max_length=255,
        validators=(MinLengthValidator(1),),
        unique=True
    )

    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def to_dict(self):
        return {
            "pk": self.pk,
            "name": self.name,
            "score": self.score
        }

    def __repr__(self):
        return "{}. ".format(self.pk)

    __str__ = __repr__
