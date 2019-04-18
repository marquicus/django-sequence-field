from django.utils.translation import ugettext_lazy as _

# Sequence Field

SEQUENCE_KEY = _('Key')
SEQUENCE_VALUE = _('Value')
SEQUENCE_TEMPLATE = _('Template')
SEQUENCE_CREATED = _('Created at')
SEQUENCE_UPDATED = _('Updated at')

SEQUENCE_MODEL_NAME = _('Sequence')
SEQUENCE_MODEL_NAME_PLURAL = _('Sequences')

SEQUENCE_FIELD_DESCRIPTION = _('Templated sequence object')

# Errors

SEQUENCE_FIELD_PATTERN_MISMATCH = _(
    'The value does not match the specified pattern'
)

SEQUENCE_FIELD_MISSING_KEY = _(
    'The key parameter is mandatory and is missing'
)

SEQUENCE_FIELD_KEY_MISMATCH = _(
    'The key \'%(key)s\' does not match any of the existing '
    'sequence model objects'
)
