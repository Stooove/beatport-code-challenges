"""
Implement a class that can convert a Python dictionary into an object.

    {
        'a': 1,
        'b': {
            'c': 2,
        },
    }

    obj.a    # should return 1
    obj.b.c  # should return 2

"""

class DictToObj:
    """Takes any level of key value pairs into a dictionary (**kwargs), then convert to objects.
    Cannot stop at nested dictionary level, ie cannot stop at 'b': {'a': 1, 'b' : {'c': 2,},...}."""
    def __init__(self, **kwargs):
        """On current level, for every key:value, make key an object and assign depth_wrap's returned value."""
        for key, value in kwargs.items():
            setattr(self, key, self.depth_wrap(value))


    def depth_wrap(self, value):
        """Check if given value is a nested dict. Return to DictToObj to make next key if it is, otherwise return value.
        Accepts value as any type."""
        return DictToObj(**value) if isinstance(value, dict) else value