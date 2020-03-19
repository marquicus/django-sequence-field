from django.test import TestCase, TransactionTestCase
from sequence_field import settings as default_settings
from sequence_field.models import Sequence
import time


class SequenceTests(TestCase):

    def test_next_sequence_default(self):
        sequence = Sequence.next(default_settings.SEQUENCE_FIELD_DEFAULT_NAME)
        self.assertEqual(sequence, '2')  # already created
        sequence = Sequence.next(default_settings.SEQUENCE_FIELD_DEFAULT_NAME)
        self.assertEqual(sequence, '3')

    def test_next_sequence_default_with_date(self):
        sequence = Sequence.next("sequence.date",
                                 '%y%m%d%NNN')
        self.assertEqual(sequence, time.strftime('%y%m%d001'))

    def test_next_sequence_default_with_param(self):
        sequence = Sequence.next("sequence.param",
                                 template='${code}%NNN',
                                 params={'code': 'NEXT'})
        self.assertEqual(sequence, 'NEXT001')

    def test_next_sequence_default_with_date_param(self):
        sequence = Sequence.next("sequence.dateparam",
                                 template='${code}%y%m%d%NNN',
                                 params={'code': 'S'})
        self.assertEqual(sequence, time.strftime('S%y%m%d001'))

    def test_next_sequence_custom_with_date_param(self):
        sequence = Sequence.next('test.sequence.1',
                                 template='%Y%m%d${code}%NNNNN',
                                 params={'code': 'XYZ'})
        self.assertEqual(sequence, time.strftime('%Y%m%dXYZ00001'))
        self.assertEqual(Sequence.objects.get(key='test.sequence.1').__str__(), "test.sequence.1:1")

    def test_next_sequence_custom_with_reset_daily(self):
        sequence = Sequence.next('test.sequence.2',
                                 template='%Y%m%d${code}%NNNNN',
                                 params={'code': 'XYZ'},
                                 reset_counter=True, reset_counter_strategy='daily')
        self.assertEqual(sequence, time.strftime('%Y%m%dXYZ00001'))  # TODO
        self.assertEqual(Sequence.objects.get(key='test.sequence.2').__str__(), "test.sequence.2:1")

    def test_next_sequence_custom_with_reset_montly(self):
        sequence = Sequence.next('test.sequence.3',
                                 template='%Y%m%d${code}%NNNNN',
                                 params={'code': 'XYZ'},
                                 reset_counter=True, reset_counter_strategy='monthly')
        self.assertEqual(sequence, time.strftime('%Y%m%dXYZ00001'))  # TODO
        self.assertEqual(Sequence.objects.get(key='test.sequence.3').__str__(), "test.sequence.3:1")

    def test_next_sequence_custom_with_reset_yearly(self):
        sequence = Sequence.next('test.sequence.4',
                                 template='%Y%m%d${code}%NNNNN',
                                 params={'code': 'XYZ'},
                                 reset_counter=True, reset_counter_strategy='yearly')
        self.assertEqual(sequence, time.strftime('%Y%m%dXYZ00001'))  # TODO
        self.assertEqual(Sequence.objects.get(key='test.sequence.4').__str__(), "test.sequence.4:1")

class TASequenceTests(TransactionTestCase):
    pass  # TODO
