import json
import copy
import utils

full_json = utils.return_json(utils.PATH_EN)
partial_json = utils.return_json(utils.PATH_FI)

# if isinstance(full_dict[key], dict) and key in partial_dict and isinstance(partial_dict[key], dict)
# Above is full check that could be used if the current one fails for some reason


def fill_partial_dict(partial_dict, full_dict):
    for key in full_dict:
        if isinstance(full_dict[key], dict) and key in partial_dict:
            fill_partial_dict(partial_dict[key], full_dict[key])
        elif key not in partial_dict:
            # print(str(full_dict[key]) + " ##")
            partial_dict[key] = str(full_dict[key]) + " ##"  # or something similar with


fill_partial_dict(partial_json, full_json)

with open(utils.PATH_FI, "w", encoding="utf-8") as f:
    json.dump(partial_json, f, ensure_ascii=False, indent=2)
