# -*- coding: utf-8 -*-

from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'A {} wrapped box of {}'.format(style, str(item()))
        return wrapped_item
    return add_wrapping

@add_wrapping_with_style('Badly')
@add_wrapping_with_style('Beautifully')
def new_dac():
    return 'a new schiit stack'

print(new_dac())