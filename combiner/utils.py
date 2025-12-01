import json
import pathlib

PATH_EN = pathlib.Path("en.json")
PATH_FI = pathlib.Path("fi.json")


def return_json(path):
    with open(path, encoding="utf-8") as f_full:
        full_json = json.load(f_full)
        return full_json
