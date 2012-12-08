from django.db import models
from django import forms

class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)

class Choices(object):
    def __init__(self, *args):
        self._choices = []
        for i, arg in enumerate(args):
            setattr(self, arg[0], i)
            self._choices.append((i, arg[1]))

    def __iter__(self):
        return iter(self._choices)

    def to_dict(self):
        '''
        Automatically converts the choices to a dictionary. Useful for type lookups.
        '''
        d = {}
        for choice in self:
            d[choice[1].lower()] = choice[0]
        return d

def get_keyvalue(intval,dictionary={}):
	for key, val in dictionary.iteritems():
		if val == intval:
			return str(key)

# Specific length for the integerfield
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class StringListField(models.Field):
    u'''
    Save a list of strings in a CharField (or TextField) column.

    In the django model object the column is a list of strings.
    '''
    __metaclass__=models.SubfieldBase
    SPLIT_CHAR=u'\v'
    def __init__(self, *args, **kwargs):
        self.internal_type=kwargs.pop('internal_type', 'CharField') # or TextField
        super(StringListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        return value.split(self.SPLIT_CHAR)

    def get_internal_type(self):
        return self.internal_type

    def get_db_prep_lookup(self, lookup_type, value):
        # SQL WHERE
        raise NotImplementedError()

    def get_db_prep_save(self, value):
        return self.SPLIT_CHAR.join(value)

    def formfield(self, **kwargs):
        assert not kwargs, kwargs
        return forms.MultipleChoiceField(choices=self.choices)

