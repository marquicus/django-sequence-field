from sequence_field import settings


def load_class(name):
    components = name.split('.')
    module_path = '.'.join(components[:-1])
    class_name = components[-1]
    mod = __import__(module_path, fromlist=[class_name])
    klass = getattr(mod, class_name)
    return klass


def expand(template, count, params={}, value=None):
    for expander_class in settings.SEQUENCE_FIELD_DEFAULT_EXPANDERS:  # statically controlled in settings
        klass = load_class(expander_class)
        expander = klass(template, count, params, value)
        value = expander.expand()
    return value
