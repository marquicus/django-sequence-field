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
        }
        self._db_type = kwargs.pop('db_type', None)
        self.evaluate_formfield = kwargs.pop('evaluate_formfield', False)

        self.lazy = kwargs.pop('lazy', True)

        try:
            self.key = kwargs.pop('key')
        except KeyError:
            self.key = settings.SEQUENCE_FIELD_DEFAULT_NAME

        default_pattern = settings.SEQUENCE_FIELD_DEFAULT_PATTERN
        self.pattern = kwargs.pop('pattern', default_pattern)

        default_template = settings.SEQUENCE_FIELD_DEFAULT_TEMPLATE
        self.template = kwargs.pop('template', default_template)

        default_expanders = settings.SEQUENCE_FIELD_DEFAULT_EXPANDERS

        self.params = kwargs.pop('params', {})

        self.expanders = kwargs.pop('expanders', default_expanders)

        self.auto = kwargs.pop('auto', False)

        kwargs['help_text'] = kwargs.get(
            'help_text', self.default_error_messages['invalid']
        )

        super(SequenceField, self).__init__(*args, **kwargs)

    def _next_value(self):
        seq = Sequence.create_if_missing(self.key, self.template)
        return seq.next_value(self.template, self.params, self.expanders)

    def pre_save(self, model_instance, add):
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """
        # Sequence.create_if_missing(self.key, self.template)
        value = getattr(model_instance, self.attname, None)
        if self.auto and add and not value:
            # Assign a new value for this attribute if required.
            sequence_string = self._next_value()
            setattr(model_instance, self.attname, sequence_string)
            value = sequence_string
        return value
