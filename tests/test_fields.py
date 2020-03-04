from django.db import models
from django.test import TestCase
from sequence_field.fields import SequenceField
from django.test.utils import isolate_apps


@isolate_apps('tests')
class SequenceFieldTests(TestCase):

    def test_model_definition(self):
        class TestModel(models.Model):
            sequence = SequenceField()
