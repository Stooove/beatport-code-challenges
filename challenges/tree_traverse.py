"""
Given a deeply nested dict, create a function that returns a
value within a tree when given the tree and a key. If there are
duplicates, the first result found should be returned.

    {
        'a': {
            'b': 123,
            'c': 456,
            'd': {
                'z': 789,
            },
        },
        'x': {
            'y': 111,
        },
    }  # input of 'z' should return '789'
"""

def tree_traverse(tree, keystore): # renamed key to keystore so iterations don't mess with target key
    """Given a deeply nested dict and key, returns value from tree. If there are duplicates,
    the first result found should be returned."""
    for key, value in tree.items():
        keystore_value_from_depth = depth_wrap(value, keystore) #check if value is a dictionary. return nothing if not dictionary or return keystore's value if it's in the nested dictionary.
        if keystore_value_from_depth != '' and not keystore_value_from_depth is None:
            return keystore_value_from_depth
        if key == keystore:
            return value


def depth_wrap(value, keystore):
    """Given value as any type, keystore as immutable data type (keystore is pass through),
    return to tree_traverse if value is a nested dictionary, otherwise return nothing."""
    return tree_traverse(value, keystore) if isinstance(value, dict) else ''