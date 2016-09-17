# -*- coding: utf-8 -*-

__version__ = '1.0.dev0'

import os
from zope.dottedname import resolve


def load(maybe_dotted, *args, **kwds):
    module = resolve.resolve(maybe_dotted)
    return CustomSettings(module, *args, **kwds)


class NoSet:
    pass


def coerce(value1, value2, default=None):
    if value1 is not NoSet:
        return value1
    elif value2 is not NoSet:
        return value1
    else:
        return default


class NoCustomSettingError(Exception):
    pass


class CustomSettings(object):
    def __init__(self, data, type_=NoSet, default=NoSet, use_environ=NoSet, raise_exception=NoSet):
        self.data = data

        self.type_ = type_
        self.default = default
        self.use_environ = use_environ
        self.raise_exception = raise_exception

    def get(self, name, type_=NoSet, default=NoSet, use_environ=NoSet, raise_exception=NoSet):
        type_ = coerce(type_, self.type_)
        default = coerce(default, self.default)
        use_environ = coerce(use_environ, self.use_environ)
        raise_exception = coerce(raise_exception, self.raise_exception)

        value = getattr(self.data, name, NoSet)
        if value is NoSet and use_environ:
            value = os.environ.get(name, use_environ, NoSet)

        if value is not NoSet and type_ is not NoSet:
            value = type_(value)

        if value is NoSet and raise_exception:
            raise NoCustomSettingError('Not been set: {}'.format(name))

        if value is NoSet:
            value = default

        return value
