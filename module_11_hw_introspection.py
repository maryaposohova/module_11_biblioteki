import inspect
import sys
from pprint import pprint


def introspection_info(obj):
    type_ = str(type(obj)).split(" ")[1].replace(">", "").replace("'", "")
    attributes_ = dir(obj)
    methods_ = sys.builtin_module_names
    module_ = sys.modules
    pprint({'type': type_,
           'attributes': attributes_, 'methods': methods_, 'module': module_})


introspection_info([1, '2'])

# def introspection_info(obj):
#     # type_ = str(type(obj)).split(' ')[1].replace('>', '')
#     # attributes_ = dir(obj)
#     # methods_ = sys.builtin_module_names
#     # module_ = sys.modules
#     # pprint({'type': type_,
#     #        'attributes': attributes_, 'methods': methods_, 'module': module_})
#     pprint({'type': type(obj),
#             'atr': dir(obj),
#             'putb': sys.path})
#
#
# introspection_info([1, 2, '3', '4'])

