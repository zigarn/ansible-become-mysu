#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import operator


def test_equalto(value, other):
    """Check if an object has the same value as another object:

    .. sourcecode:: jinja

        {% if foo.expression is equalto 42 %}
            the foo attribute evaluates to the constant 42
        {% endif %}

    This appears to be a useless test as it does exactly the same as the
    ``==`` operator, but it can be useful when used together with the
    `selectattr` function:

    .. sourcecode:: jinja

        {{ users|selectattr("email", "equalto", "foo@bar.invalid") }}

    .. versionadded:: 2.8
    """
    return value == other


class TestModule(object):
    ''' Backport Jinja2 2.8 equalto tests '''

    def tests(self):
        return {
            'equalto': test_equalto,
        }
