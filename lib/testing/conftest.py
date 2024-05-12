#!/usr/bin/env python3

def pytest_itemcollected(item):
    parent_object = item.parent.obj
    node_object = item.obj

    # Get the prefix (parent's docstring or class name)
    prefix = parent_object.__doc__.strip() if parent_object.__doc__ else parent_object.__class__.__name__

    # Get the suffix (node's docstring or function name)
    suffix = node_object.__doc__.strip() if node_object.__doc__ else node_object.__name__

    # Construct the node ID with a space separator
    node_id = f"{prefix} {suffix}" if prefix or suffix else None

    if node_id:
        item._nodeid = node_id
