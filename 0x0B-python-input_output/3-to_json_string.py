#!/user/bin/python3
# 3-to_json_string.py

"""To  Json STRING"""


def to_json_string(my_obj):
    """
    a function that returns a JSON rep of an obj
    args:
        my_obj - the object rep
    """
    import json
    f = json.dumps(my_obj)
    return f
