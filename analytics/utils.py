# coding: utf-8
import os
import re
import unicodedata
import weakref

from datetime import datetime

try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import ConfigParser as SafeConfigParser

REGEX_ISSN = re.compile("^[0-9]{4}-[0-9]{3}[0-9xX]$")
REGEX_ISSUE = re.compile("^[0-9]{4}-[0-9]{3}[0-9xX][0-2][0-9]{3}[0-9]{4}$")
REGEX_ARTICLE = re.compile("^S[0-9]{4}-[0-9]{3}[0-9xX][0-2][0-9]{3}[0-9]{4}[0-9]{5}$")


def dogpile_controller_key_generator(namespace, fn, *kwargs):

    fname = fn.__name__

    def generate_key(*the_args, **the_kwargs):

        tp = tuple([
            str(namespace),
            str(fname),
            str(the_args[1:]),
            tuple(the_kwargs.items())
        ])

        return str(hash(str(tp)))

    return generate_key


def clean_string(text):

    if isinstance(text, str):
        try:
            text = text.decode('utf-8')
        except:
            pass

    try:
        nfd_form = unicodedata.normalize('NFD', text.strip().lower())
    except:
        return text

    cleaned_str = u''.join(x for x in nfd_form if unicodedata.category(x)[0] == 'L' or x == ' ')

    return cleaned_str.lower().strip()


def mktime(year=1970, month=1, day=1):

    epoch = datetime(1970, 1, 1)
    diff = datetime(year, month, day) - epoch

    return diff.total_seconds() * 1000


def convert_date_to_month_start_unix_ms(date):
    fmt_date = datetime.strptime(date, '%Y-%m-%d')
    fmt_date = fmt_date.replace(day = 1)

    ms_unix_epoch = int(fmt_date.timestamp() * 1000)

    return ms_unix_epoch


class SingletonMixin(object):
    """
    Adds a singleton behaviour to an existing class.

    weakrefs are used in order to keep a low memory footprint.
    As a result, args and kwargs passed to classes initializers
    must be of weakly refereable types.
    """
    _instances = weakref.WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        key = (cls, args, tuple(kwargs.items()))

        if key in cls._instances:
            return cls._instances[key]

        new_instance = super(type(cls), cls).__new__(cls, *args, **kwargs)
        cls._instances[key] = new_instance

        return new_instance


class Configuration(SingletonMixin):
    """
    Acts as a proxy to the ConfigParser module
    """
    def __init__(self, fp, parser_dep=SafeConfigParser):
        self.conf = parser_dep()
        self.conf.readfp(fp)

    @classmethod
    def from_env(cls):
        try:
            filepath = os.environ['ANALYTICS_SETTINGS_FILE']
        except KeyError:
            raise ValueError('missing env variable ANALYTICS_SETTINGS_FILE')

        return cls.from_file(filepath)

    @classmethod
    def from_file(cls, filepath):
        """
        Returns an instance of Configuration

        ``filepath`` is a text string.
        """
        fp = open(filepath, 'rb')
        return cls(fp)

    def __getattr__(self, attr):
        return getattr(self.conf, attr)

    def items(self):
        """Settings as key-value pair.
        """
        return [(section, dict(self.conf.items(section, raw=True))) for
                section in [section for section in self.conf.sections()]]
