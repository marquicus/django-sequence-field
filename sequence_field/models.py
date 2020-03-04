from django.db import models
from sequence_field import utils
from sequence_field import strings
from sequence_field import constants
from sequence_field import settings
from django.utils import timezone


class Sequence(models.Model):

    key = models.CharField(
        verbose_name=strings.SEQUENCE_KEY,
        max_length=constants.SEQUENCE_KEY_LENGTH,
        unique=True
    )

    value = models.PositiveIntegerField(
        verbose_name=strings.SEQUENCE_VALUE,
        default=settings.SEQUENCE_FIELD_DEFAULT_VALUE
    )

    template = models.CharField(
        verbose_name=strings.SEQUENCE_TEMPLATE,
        max_length=constants.SEQUENCE_TEMPLATE_LENGTH,
        default=settings.SEQUENCE_FIELD_DEFAULT_TEMPLATE
    )

    created = models.DateTimeField(
        verbose_name=strings.SEQUENCE_CREATED,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name=strings.SEQUENCE_UPDATED,
        auto_now=True
    )

    def increment(self, commit=True, **kwargs):
        def diff_days(d1, d2):
            return (timezone.localtime() - self.updated).days

        def diff_months(d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month

        reset_counter = kwargs.pop('reset_counter', False)
        reset_counter_strategy = kwargs.pop('reset_counter_strategy', "daily")
        if reset_counter:
            if reset_counter_strategy == "daily":
                if diff_days(timezone.localtime(), self.updated) > 0:
                    self.value = 0
            elif reset_counter_strategy == "monthly":
                if diff_months(timezone.localtime(), self.updated) > 0:
                    self.value = 0
            elif reset_counter_strategy == "yearly":
                if diff_days(timezone.localtime(), self.updated) > 365:
                    self.value = 0
        self.value += 1
        if commit:
            self.save()

    def next_value(self,
                   template=settings.SEQUENCE_FIELD_DEFAULT_TEMPLATE,
                   params={},
                   commit=True, **kwargs):
        self.increment(commit, **kwargs)
        return utils.expand(template, self.value, params)

    @classmethod
    def next(cls, key,
             template=settings.SEQUENCE_FIELD_DEFAULT_TEMPLATE,
             params={},
             commit=True, **kwargs):
        seq, _ = Sequence.objects.get_or_create(key=key, defaults={"template": template})
        return seq.next_value(template, params, commit, **kwargs)

    class Meta:
        verbose_name = strings.SEQUENCE_MODEL_NAME
        verbose_name_plural = strings.SEQUENCE_MODEL_NAME_PLURAL

    def __str__(self):
        return self.key
