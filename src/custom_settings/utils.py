# -*- coding: utf-8 -*-


class NoSet:
    pass


def coerce(value1, value2, default=None):
    if value1 is not NoSet:
        return value1
    elif value2 is not NoSet:
        return value1
    else:
        return default
