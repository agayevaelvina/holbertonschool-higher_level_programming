#!/usr/bin/python3
"x"

def from_json_string(my_str):
    """ Returns the Python object represented by a JSON string.Args:my_str (str): JSON string to deserialize.Returns:object: Python data structure represented by the JSON string. """
    

    import json
    return json.loads(my_str)
