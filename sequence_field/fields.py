# -*- coding: utf-8 -*-

from django.db import models
from sequence_field.models import Sequence
from sequence_field import settings
from sequence_field import strings


class SequenceField(models.TextField):
    """ Stores sequence values based on templates. """

    description = strings.SEQUENCE_FIELD_DESCRIPTION

    def __init__(self, *args, **kwargs):
        self.default_error_messages = {
            'invalid': strings.SEQUENCE_FIELD_PATTERN_MISMATCH
        }  # Use case?
        self._db_type = kwargs.pop('db_type', None)  # Use case?
        self.evaluate_formfield = kwargs.pop('evaluate_formfield', False)  # Use case?
        self.lazy = kwargs.pop('lazy', True)  # Use case?
        self.key = kwargs.pop('key', settings.SEQUENCE_FIELD_DEFAULT_NAME)
        self.pattern = kwargs.pop('pattern', settings.SEQUENCE_FIELD_DEFAULT_PATTERN)
        self.template = kwargs.pop('template', settings.SEQUENCE_FIELD_DEFAULT_TEMPLATE)
        self.params = kwargs.pop('params', {})
        self.auto = kwargs.pop('auto', False)  # Use case?
        self.reset_counter = kwargs.pop('reset_counter', False)
        self.reset_counter_strategy = kwargs.pop('reset_counter_strategy', "daily")

        kwargs['help_text'] = kwargs.get(
            'help_text', self.default_error_messages['invalid']
        )  # Use case?

        super(SequenceField, self).__init__(*args, **kwargs)

    def _next_value(self):
        kwargs = {}
        kwargs["key"] = self.key
        kwargs["template"] = self.template
        kwargs["params"] = self.params
        kwargs["reset_counter"] = self.reset_counter
        kwargs["reset_counter_strategy"] = self.reset_counter_strategy
        kwargs["commit"] = True
        return Sequence.next(**kwargs)

    def pre_save(self, model_instance, add):
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """
        value = getattr(model_instance, self.attname, None)
        if self.auto and add and not value:
            # Assign a new value for this attribute if required.
            sequence_string = self._next_value()
            setattr(model_instance, self.attname, sequence_string)
            value = sequence_string
        return value
