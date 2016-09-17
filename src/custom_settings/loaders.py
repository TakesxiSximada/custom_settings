# -*- coding: utf-8 -*-
from zope.dottedname import resolve

from . import (
    adapters,
    exc,
    )


def load(maybe_dotted, *args, **kwds):
    try:
        module = resolve.resolve(maybe_dotted)
    except ImportError:
        raise exc.NoCustomSettingModuleError(
            'Cannot import custom settings module: {}'.format(maybe_dotted))
    return adapters.CustomSettings(module, *args, **kwds)
